param(
    [Parameter(Position = 0)]
    [ValidateSet("doctor", "init", "prepare", "catalog", "analyze", "migrate", "audit", "status", "update")]
    [string]$Command = "status",

    [Parameter(Position = 1)]
    [string]$ProjectName,

    [ValidateSet("ppt169", "ppt43", "xhs", "story")]
    [string]$Format = "ppt169",

    [string[]]$Source,

    [string]$Manifest,

    [string]$Pptx,

    [switch]$Strict
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$env:PYTHONIOENCODING = "utf-8"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$VendorRoot = Join-Path $RepoRoot ".vendor\ppt-master"
$CoreDir = Join-Path $VendorRoot "skills\ppt-master"
$ProjectManager = Join-Path $CoreDir "scripts\project_manager.py"
$CurrentProjectFile = Join-Path $RepoRoot "CURRENT_PROJECT.txt"
$LocalSkill = Join-Path $RepoRoot ".codex\skills\engineering-ppt"
$ProjectContract = Join-Path $LocalSkill "scripts\project_contract.py"
$SourceCatalog = Join-Path $LocalSkill "scripts\build_source_catalog.py"
$ContentBlueprint = Join-Path $LocalSkill "scripts\build_ppt_content_blueprint.py"
$ReleaseAudit = Join-Path $LocalSkill "scripts\release_audit.py"
$LegacyMigration = Join-Path $LocalSkill "scripts\migrate_legacy_manifest.py"
$TableIr = Join-Path $LocalSkill "scripts\table_ir.py"
$TableRenderers = Join-Path $LocalSkill "scripts\table_renderers.py"

function Resolve-Python {
    $fileCandidates = @(
        (Join-Path $RepoRoot ".venv\Scripts\python.exe"),
        (Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe")
    )
    foreach ($candidate in $fileCandidates) {
        if (Test-Path -LiteralPath $candidate) {
            return $candidate
        }
    }

    foreach ($commandName in @("python", "python3", "py")) {
        $cmd = Get-Command $commandName -ErrorAction SilentlyContinue
        if ($cmd) {
            return $cmd.Source
        }
    }

    throw "Python 3.10+ was not found on PATH."
}

function Resolve-ProjectName {
    if ($ProjectName) {
        return $ProjectName.Trim()
    }
    if (Test-Path -LiteralPath $CurrentProjectFile) {
        $name = (Get-Content -LiteralPath $CurrentProjectFile -Raw -Encoding UTF8).Trim()
        if ($name) {
            return $name
        }
    }
    throw "Project name is required, or CURRENT_PROJECT.txt must contain one."
}

function Resolve-ProjectPath {
    $name = Resolve-ProjectName
    if (Test-Path -LiteralPath $name -PathType Container) {
        return (Resolve-Path -LiteralPath $name).Path
    }
    return (Join-Path (Join-Path $RepoRoot "projects") $name)
}

function Invoke-CheckedPython {
    param(
        [string]$Python,
        [string[]]$Arguments
    )
    & $Python @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Python command failed with exit code $LASTEXITCODE`: $($Arguments -join ' ')"
    }
}

function Get-VendorCommit {
    if (-not (Test-Path -LiteralPath (Join-Path $VendorRoot ".git"))) {
        return "missing"
    }
    $safe = $VendorRoot.Replace("\", "/")
    return (& git -c "safe.directory=$safe" -C $VendorRoot rev-parse --short HEAD 2>$null)
}

switch ($Command) {
    "doctor" {
        $python = Resolve-Python
        $version = & $python --version
        $required = @(
            (Join-Path $CoreDir "SKILL.md"),
            $ProjectManager,
            (Join-Path $CoreDir "scripts\svg_quality_checker.py"),
            (Join-Path $CoreDir "scripts\svg_to_pptx.py"),
            $ProjectContract,
            $SourceCatalog,
            $ContentBlueprint,
            $ReleaseAudit,
            $LegacyMigration,
            $TableIr,
            $TableRenderers
        )
        $missing = @($required | Where-Object { -not (Test-Path -LiteralPath $_) })
        if ($missing.Count -gt 0) {
            throw "ppt-master kernel is incomplete:`n$($missing -join "`n")"
        }

        $importProbe = "import pptx, fitz, PIL, numpy, openpyxl, requests, bs4, flask"
        & $python -c $importProbe
        if ($LASTEXITCODE -ne 0) {
            throw "Python dependencies are incomplete. Run: $python -m pip install -r `"$CoreDir\requirements.txt`""
        }

        Write-Output "Repository: $RepoRoot"
        Write-Output "Python: $version ($python)"
        Write-Output "ppt-master commit: $(Get-VendorCommit)"
        Write-Output "Core skill: $CoreDir"
        Write-Output "Engineering skill: $LocalSkill"
        Write-Output "Dependencies: ready"
        Write-Output "Status: ready"
    }

    "init" {
        $python = Resolve-Python
        $name = Resolve-ProjectName
        $projectPath = Join-Path (Join-Path $RepoRoot "projects") $name

        Invoke-CheckedPython -Python $python -Arguments @($ProjectContract, $projectPath, "--name", $name, "--format", $Format)

        Set-Content -LiteralPath $CurrentProjectFile -Value $name -Encoding UTF8
        Write-Output "Current project: $name"
        Write-Output "Project path: $projectPath"
        Write-Output "Canvas format requested: $Format"
    }

    "prepare" {
        $python = Resolve-Python
        $projectPath = Resolve-ProjectPath
        Invoke-CheckedPython -Python $python -Arguments @($ProjectContract, $projectPath)
        Write-Output "Contracts ready: $projectPath"
    }

    "catalog" {
        $python = Resolve-Python
        $projectPath = Resolve-ProjectPath
        Invoke-CheckedPython -Python $python -Arguments @($ProjectContract, $projectPath)
        $arguments = @($SourceCatalog, $projectPath)
        if ($Source) {
            foreach ($sourcePath in $Source) {
                if ($sourcePath) {
                    $arguments += @("--source", $sourcePath)
                }
            }
        }
        Invoke-CheckedPython -Python $python -Arguments $arguments
    }

    "analyze" {
        $python = Resolve-Python
        $projectPath = Resolve-ProjectPath
        Invoke-CheckedPython -Python $python -Arguments @($ProjectContract, $projectPath)
        if (-not (Test-Path -LiteralPath (Join-Path $projectPath "analysis\source_catalog.json"))) {
            throw "Run catalog before analyze: scripts\ppt-agent.cmd catalog `"$((Resolve-ProjectName))`""
        }
        Invoke-CheckedPython -Python $python -Arguments @($ContentBlueprint, $projectPath)
    }

    "migrate" {
        $python = Resolve-Python
        $projectPath = Resolve-ProjectPath
        if (-not $Manifest) {
            throw "Use -Manifest <slide_manifest.json> for legacy migration."
        }
        Invoke-CheckedPython -Python $python -Arguments @($ProjectContract, $projectPath)
        Invoke-CheckedPython -Python $python -Arguments @($LegacyMigration, $projectPath, $Manifest)
        Write-Output "Legacy manifest migrated. All evidence remains needs-verification."
    }

    "audit" {
        $python = Resolve-Python
        $projectPath = Resolve-ProjectPath
        $arguments = @($ReleaseAudit, $projectPath)
        if ($Strict) {
            $arguments += "--strict"
        }
        if ($Pptx) {
            $arguments += @("--pptx", $Pptx)
        }
        Invoke-CheckedPython -Python $python -Arguments $arguments
    }

    "status" {
        $name = Resolve-ProjectName
        $projectPath = Resolve-ProjectPath
        Write-Output "Current project: $name"
        Write-Output "Project path: $projectPath"
        Write-Output "Exists: $(Test-Path -LiteralPath $projectPath)"
        Write-Output "ppt-master commit: $(Get-VendorCommit)"

        foreach ($item in @(
            "analysis\source_catalog.json",
            "analysis\table_ir.json",
            "analysis\report_content_inventory.json",
            "analysis\ppt_content_blueprint.md",
            "project_config.json",
            "evidence_ledger.json",
            "deck_plan.json",
            "source_map.md",
            "chapter_coverage.md",
            "claim_spine.md",
            "design_spec.md",
            "spec_lock.md",
            "tables",
            "svg_output",
            "qa\release_audit.json",
            "exports"
        )) {
            $path = Join-Path $projectPath $item
            Write-Output ("{0}: {1}" -f $item, (Test-Path -LiteralPath $path))
        }
    }

    "update" {
        if (-not (Test-Path -LiteralPath (Join-Path $VendorRoot ".git"))) {
            throw "Vendored ppt-master repository is missing: $VendorRoot"
        }
        $safe = $VendorRoot.Replace("\", "/")
        & git -c "safe.directory=$safe" -C $VendorRoot pull --ff-only
        if ($LASTEXITCODE -ne 0) {
            throw "Unable to update ppt-master."
        }
        Write-Output "ppt-master commit: $(Get-VendorCommit)"
    }
}
