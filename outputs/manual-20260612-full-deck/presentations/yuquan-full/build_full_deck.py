import base64
import html
import json
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
PROJECT = ROOT / "projects" / "当阳玉泉水库"
OUT = PROJECT / "full_deck" / "svg_final"
MEDIA = PROJECT / "qa" / "report-docx-package" / "word" / "media"

W, H = 1280, 720
NAVY = "#0B3558"
TEAL = "#0E9F9A"
GREEN = "#63A35C"
ORANGE = "#E8923A"
RED = "#C94B45"
INK = "#17324A"
MUTED = "#64798A"
PAPER = "#F5F3EC"
WHITE = "#FFFFFF"
LINE = "#C8D3D9"
PALE = "#E8F1F2"
FONT = "Microsoft YaHei, Arial, sans-serif"


def esc(value):
    return html.escape(str(value))


def wrap(text, width):
    return textwrap.wrap(str(text), width=width, break_long_words=False, break_on_hyphens=False)


def svg_open(bg=PAPER):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        f'<rect width="{W}" height="{H}" fill="{bg}"/>',
    ]


def svg_close(parts):
    parts.append("</svg>")
    return "\n".join(parts)


def text(parts, x, y, value, size=24, fill=INK, weight="normal", anchor="start", family=FONT):
    parts.append(
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{esc(value)}</text>'
    )


def multiline(parts, x, y, value, size=22, fill=INK, width=34, line_h=1.45, weight="normal"):
    for i, line in enumerate(wrap(value, width)):
        text(parts, x, y + i * size * line_h, line, size, fill, weight)


def header(parts, number, chapter, title, dark=False):
    fg = WHITE if dark else INK
    sub = "#B9D6E5" if dark else MUTED
    parts.append(f'<rect x="54" y="48" width="8" height="30" fill="{TEAL}"/>')
    text(parts, 78, 72, f"{chapter}  |  {number:02d}", 15, sub, "bold")
    multiline(parts, 54, 122, title, 34, fg, 31, 1.2, "bold")


def footer(parts, source, number, dark=False):
    color = "#B9D6E5" if dark else MUTED
    parts.append(f'<line x1="54" y1="672" x2="1226" y2="672" stroke="{color}" stroke-opacity=".35"/>')
    text(parts, 54, 698, source, 11, color)
    text(parts, 1226, 698, f"{number:02d}", 12, color, "bold", "end")


def metric(parts, x, y, value, label, color=TEAL, w=250):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="122" rx="10" fill="{WHITE}" stroke="{LINE}"/>')
    text(parts, x + 20, y + 50, value, 34, color, "bold")
    multiline(parts, x + 20, y + 82, label, 15, MUTED, 18, 1.3)


def card(parts, x, y, w, h, title_value, body, accent=TEAL, index=None):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{WHITE}" stroke="{LINE}"/>')
    parts.append(f'<rect x="{x}" y="{y}" width="7" height="{h}" rx="3" fill="{accent}"/>')
    if index is not None:
        text(parts, x + 28, y + 38, f"{index:02d}", 16, accent, "bold")
        ty = y + 70
    else:
        ty = y + 42
    multiline(parts, x + 28, ty, title_value, 20, INK, 18, 1.25, "bold")
    multiline(parts, x + 28, ty + 52, body, 15, MUTED, max(16, int(w / 14)), 1.45)


def data_uri(path):
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def make_cover(slide):
    p = svg_open(NAVY)
    p += [
        f'<circle cx="1110" cy="115" r="250" fill="{TEAL}" fill-opacity=".18"/>',
        f'<circle cx="1180" cy="620" r="340" fill="{GREEN}" fill-opacity=".12"/>',
        '<path d="M0 565 C250 505 400 655 660 590 C910 528 1050 570 1280 490 L1280 720 L0 720 Z" fill="#FFFFFF" fill-opacity=".07"/>',
        f'<rect x="70" y="92" width="86" height="8" fill="{TEAL}"/>',
    ]
    text(p, 70, 145, "水资源论证 · 完整章节汇报", 18, "#B9D6E5", "bold")
    text(p, 70, 270, "玉泉水库灌区", 58, WHITE, "bold")
    text(p, 70, 345, "水资源论证报告", 58, WHITE, "bold")
    multiline(p, 72, 405, "按报告九章体系展开，讲清需水、供水、影响与管理闭环", 23, "#DCE8EF", 35)
    metric(p, 70, 505, "49 页", "完整汇报结构", TEAL, 230)
    metric(p, 320, 505, "9 章", "对应报告正文", GREEN, 230)
    metric(p, 570, 505, "P=90%", "灌溉设计保证率", ORANGE, 230)
    text(p, 70, 660, "建设单位：当阳市惠清水环境治理有限责任公司", 14, "#B9D6E5")
    text(p, 1210, 660, "2026 年 6 月", 14, "#B9D6E5", anchor="end")
    return svg_close(p)


def make_divider(slide):
    p = svg_open(NAVY)
    n = slide["number"]
    p += [
        f'<circle cx="1040" cy="360" r="250" fill="{TEAL}" fill-opacity=".12"/>',
        f'<rect x="72" y="118" width="90" height="8" fill="{TEAL}"/>',
    ]
    text(p, 72, 200, f"CHAPTER {slide['chapter_no']}", 18, "#9FC8D7", "bold")
    multiline(p, 72, 305, slide["title"], 54, WHITE, 16, 1.18, "bold")
    multiline(p, 75, 430, slide["subtitle"], 23, "#D5E4EA", 34, 1.5)
    text(p, 1160, 625, f"{n:02d}", 72, "#6DB9B3", "bold", "end")
    return svg_close(p)


def make_agenda(slide):
    p = svg_open()
    header(p, slide["number"], "汇报导览", slide["title"])
    for i, item in enumerate(slide["items"]):
        row = i // 3
        col = i % 3
        x = 54 + col * 390
        y = 205 + row * 150
        card(p, x, y, 355, 118, item[0], item[1], [TEAL, GREEN, ORANGE][col], i + 1)
    footer(p, slide["source"], slide["number"])
    return svg_close(p)


def make_metrics(slide):
    p = svg_open()
    header(p, slide["number"], slide["chapter"], slide["title"])
    for i, item in enumerate(slide["metrics"]):
        metric(p, 54 + i * 290, 205, item[0], item[1], item[2], 265)
    if slide.get("bullets"):
        y = 390
        for i, bullet in enumerate(slide["bullets"]):
            p.append(f'<circle cx="72" cy="{y + i*62 - 7}" r="6" fill="{TEAL}"/>')
            multiline(p, 92, y + i * 62, bullet, 19, INK, 52, 1.35)
    footer(p, slide["source"], slide["number"])
    return svg_close(p)


def make_cards(slide):
    p = svg_open()
    header(p, slide["number"], slide["chapter"], slide["title"])
    items = slide["cards"]
    cols = 2 if len(items) <= 4 else 3
    w = 560 if cols == 2 else 360
    h = 180 if len(items) <= 4 else 150
    for i, item in enumerate(items):
        x = 54 + (i % cols) * (w + 38)
        y = 205 + (i // cols) * (h + 28)
        card(p, x, y, w, h, item[0], item[1], item[2] if len(item) > 2 else TEAL, i + 1)
    footer(p, slide["source"], slide["number"])
    return svg_close(p)


def make_bars(slide):
    p = svg_open()
    header(p, slide["number"], slide["chapter"], slide["title"])
    values = slide["values"]
    maxv = max(v[1] for v in values) or 1
    y0 = 220
    for i, (label, value, unit, color) in enumerate(values):
        y = y0 + i * 70
        text(p, 54, y + 20, label, 17, INK, "bold")
        p.append(f'<rect x="260" y="{y}" width="760" height="30" rx="5" fill="#DDE6E9"/>')
        bw = 760 * value / maxv
        p.append(f'<rect x="260" y="{y}" width="{bw:.1f}" height="30" rx="5" fill="{color}"/>')
        text(p, 1040, y + 23, f"{value:g}{unit}", 18, color, "bold")
    if slide.get("note"):
        p.append(f'<rect x="54" y="575" width="1135" height="66" rx="8" fill="{PALE}"/>')
        multiline(p, 76, 607, slide["note"], 16, INK, 68, 1.3, "bold")
    footer(p, slide["source"], slide["number"])
    return svg_close(p)


def make_flow(slide):
    p = svg_open()
    header(p, slide["number"], slide["chapter"], slide["title"])
    items = slide["items"]
    x0 = 54
    y = 265
    bw = (1120 - (len(items) - 1) * 70) / len(items)
    for i, item in enumerate(items):
        x = x0 + i * (bw + 70)
        p.append(f'<rect x="{x}" y="{y}" width="{bw}" height="190" rx="12" fill="{WHITE}" stroke="{LINE}"/>')
        p.append(f'<rect x="{x}" y="{y}" width="{bw}" height="10" rx="5" fill="{item[2]}"/>')
        text(p, x + 22, y + 55, item[0], 25, item[2], "bold")
        multiline(p, x + 22, y + 98, item[1], 16, MUTED, max(12, int(bw / 14)), 1.45)
        if i < len(items) - 1:
            ax = x + bw + 18
            p.append(f'<line x1="{ax}" y1="{y+95}" x2="{ax+34}" y2="{y+95}" stroke="{TEAL}" stroke-width="4"/>')
            p.append(f'<path d="M{ax+34} {y+95} l-10 -8 v16 z" fill="{TEAL}"/>')
    if slide.get("note"):
        multiline(p, 54, 555, slide["note"], 18, INK, 67, 1.4, "bold")
    footer(p, slide["source"], slide["number"])
    return svg_close(p)


def make_image(slide):
    p = svg_open()
    header(p, slide["number"], slide["chapter"], slide["title"])
    uri = data_uri(MEDIA / slide["image"])
    p.append(f'<rect x="54" y="190" width="720" height="440" rx="10" fill="{WHITE}" stroke="{LINE}"/>')
    p.append(
        f'<image x="66" y="202" width="696" height="416" preserveAspectRatio="xMidYMid meet" href="{uri}"/>'
    )
    y = 215
    for i, item in enumerate(slide["bullets"]):
        card(p, 810, y + i * 130, 390, 108, item[0], item[1], item[2], i + 1)
    footer(p, slide["source"], slide["number"])
    return svg_close(p)


def make_matrix(slide):
    p = svg_open()
    header(p, slide["number"], slide["chapter"], slide["title"])
    rows = slide["rows"]
    x0, y0 = 54, 205
    widths = [220, 300, 300, 300]
    headers = slide["headers"]
    x = x0
    for i, head in enumerate(headers):
        p.append(f'<rect x="{x}" y="{y0}" width="{widths[i]}" height="54" fill="{NAVY}"/>')
        text(p, x + 14, y0 + 35, head, 16, WHITE, "bold")
        x += widths[i]
    for r, row in enumerate(rows):
        y = y0 + 54 + r * 72
        x = x0
        for c, cell in enumerate(row):
            fill = WHITE if r % 2 == 0 else "#EDF2F3"
            p.append(f'<rect x="{x}" y="{y}" width="{widths[c]}" height="72" fill="{fill}" stroke="{LINE}"/>')
            multiline(p, x + 14, y + 28, cell, 14, INK if c else TEAL, max(10, int(widths[c] / 13)), 1.25, "bold" if c == 0 else "normal")
            x += widths[c]
    footer(p, slide["source"], slide["number"])
    return svg_close(p)


SLIDES = [
    {"number": 1, "type": "cover", "title": "玉泉水库灌区水资源论证报告"},
    {"number": 2, "type": "metrics", "chapter": "核心结论", "title": "方案可行的前提，是把联合补源、指标落实和全过程监管同时锁定",
     "metrics": [("750 万m³", "年申请取水量", TEAL), ("1.762 万亩", "覆盖三村灌溉面积", GREEN), ("90%", "灌溉设计保证率", ORANGE), ("150 万m³", "年回归退水量", NAVY)],
     "bullets": ["玉泉水库自身来水不足，必须与东风三干渠形成引蓄联合调度。", "2024 年总量指标静态余量约 563 万m³，许可阶段需明确 750 万m³的指标来源与统筹口径。", "报告若干计算表存在正文缺数或两组口径，正式报批前应以最终签章表格统一。"],
     "source": "来源：报告基本情况表、第4—5章、第9章"},
    {"number": 3, "type": "agenda", "title": "九章报告形成“背景—核算—影响—管控—结论”的完整证据链",
     "items": [("1 总论", "任务、依据、等级与范围"), ("2 项目概况", "工程边界与取退水方案"), ("3 区域水资源", "资源条件、开发现状与潜力"), ("4 用水合理性", "需水、供需平衡与核定"), ("5 取水水源", "水源可靠性与取水口"), ("6 取水影响", "资源、生态及第三方"), ("7 退水影响", "回归水路径与环境影响"), ("8 管理措施", "节约、保护和长效管理"), ("9 结论建议", "审批条件与后续工作")],
     "source": "来源：报告目录"},
    {"number": 4, "type": "divider", "chapter_no": "01", "title": "总论", "subtitle": "明确为什么论证、依据什么论证，以及本次论证覆盖哪些空间和时间边界。"},
    {"number": 5, "type": "flow", "chapter": "第1章 总论", "title": "论证工作从现场踏勘开始，以取水许可技术支撑为终点",
     "items": [("2026.04", "现场踏勘水源地、取水口与周边环境，收集法规、规划和水资源资料。", TEAL), ("资料分析", "评价区域资源状况、开发利用程度、需水合理性和水源可靠性。", GREEN), ("影响论证", "识别取水、退水对水资源、水环境和其他用户的影响。", ORANGE), ("2026.05", "形成送审稿，为水行政主管部门审批取水许可提供依据。", NAVY)],
     "source": "来源：报告1.1"},
    {"number": 6, "type": "cards", "chapter": "第1章 总论", "title": "五项任务共同回答“能不能取、取多少、如何管”",
     "cards": [("划定边界", "确定分析范围、水源论证范围及取退水影响范围。", TEAL), ("判断合理性", "对照产业政策、规划、配置方案与用水定额。", GREEN), ("验证可靠性", "核算来水、可供水量、联合调度和保证率。", ORANGE), ("评估影响", "分析资源、生态、水功能区及其他用水户影响。", NAVY), ("提出措施", "形成节约、保护、监测、调度和补偿建议。", RED)],
     "source": "来源：报告1.2"},
    {"number": 7, "type": "cards", "chapter": "第1章 总论", "title": "论证依据由法律制度、技术标准和区域资料三层构成",
     "cards": [("法律与许可制度", "《水法》、取水许可条例、论证管理办法、最严格水资源管理制度。", NAVY), ("水资源技术标准", "GB/T35580-2017、SL/T769-2020、供需平衡与水利计算规范。", TEAL), ("用水与环境标准", "湖北省农业用水定额、农田灌溉水质标准、地表水环境质量标准。", GREEN), ("区域成果资料", "2024年水资源公报、环境质量年报、国土空间与流域治理规划。", ORANGE)],
     "source": "来源：报告1.3"},
    {"number": 8, "type": "image", "chapter": "第1章 总论", "title": "二级论证覆盖四类空间边界，现状年2024、规划年2034",
     "image": "image21.jpeg",
     "bullets": [("分析范围", "当阳市行政范围 2149.71 km²", TEAL), ("水源范围", "玉泉水库坝址以上 4.00 km²流域", GREEN), ("影响范围", "取水为水库水域；退水为三村灌区", ORANGE)],
     "source": "来源：报告1.4—1.5、附图一"},
    {"number": 9, "type": "divider", "chapter_no": "02", "title": "建设项目概况", "subtitle": "说明工程服务对象、政策属性、取水工程和农业回归水方案。"},
    {"number": 10, "type": "metrics", "chapter": "第2章 项目概况", "title": "项目以农业灌溉为核心，兼顾防洪与生态功能",
     "metrics": [("小（1）型", "报告项目定位", NAVY), ("3 个村", "子龙、合意、玉泉", TEAL), ("17,621.55 亩", "农田总面积", GREEN), ("11–15 km", "距当阳市区约", ORANGE)],
     "bullets": ["主要作物包括水稻、油菜、小麦、玉米及蔬菜。", "供水目标单一明确，为当地粮食稳产和农业抗旱提供水源保障。"],
     "source": "来源：报告2.1、3.1.4"},
    {"number": 11, "type": "matrix", "chapter": "第2章 项目概况", "title": "项目与产业政策、区域规划和水功能管理要求总体相符",
     "headers": ["审查维度", "依据", "项目响应", "判断"],
     "rows": [("产业政策", "产业结构调整指导目录", "公益性农田水利与水资源优化配置", "鼓励类"),
              ("乡村振兴", "粮食安全与高标准农田", "提升灌溉保证率和农业综合生产能力", "相符"),
              ("国土空间", "当阳市国土空间规划", "现有水库与渠系，不新增敏感占用", "相符"),
              ("流域治理", "四水共治与水安全底线", "联合配置、生态下泄、面源管控", "相符"),
              ("水功能管理", "最严格水资源管理制度", "定额、计量、监测和影响控制", "有条件相符")],
     "source": "来源：报告2.2"},
    {"number": 12, "type": "flow", "chapter": "第2章 项目概况", "title": "取水依托既有闸渠系统，退水遵循农业水循环路径",
     "items": [("联合水源", "玉泉水库本地径流 + 东风三干渠补源", TEAL), ("取水控制", "坝址节制闸，最大流量0.81 m³/s", NAVY), ("输配水", "既有干支渠、量水堰与远程闸门", GREEN), ("农业回归水", "按20%估算，沟渠漫流和土壤下渗", ORANGE)],
     "note": "日最大取水量 7.02 万m³；年退水量 150 万m³；主要关注 COD、氨氮及氮磷面源风险。",
     "source": "来源：报告2.3—2.4、基本情况表"},
    {"number": 13, "type": "divider", "chapter_no": "03", "title": "水资源及其开发利用状况", "subtitle": "把项目放入当阳市资源禀赋、供水体系、用水结构和总量控制的大背景中审视。"},
    {"number": 14, "type": "image", "chapter": "第3章 区域背景", "title": "项目位于沮漳河流域玉泉河中游，靠近农业需水区",
     "image": "image9.jpeg",
     "bullets": [("区域位置", "当阳市中西部、玉泉街道境内", TEAL), ("流域关系", "沮河一级支流玉泉河中游", NAVY), ("供水对象", "子龙、合意、玉泉三村农田", GREEN)],
     "source": "来源：报告3.1.1、附图五"},
    {"number": 15, "type": "metrics", "chapter": "第3章 区域背景", "title": "农业规模决定了灌溉保供具有明确的公共效益",
     "metrics": [("41.9 万人", "2024年常住人口", NAVY), ("244.95 亿元", "农林牧渔业总产值", TEAL), ("84.9 千公顷", "粮食种植面积", GREEN), ("47.6 万吨", "粮食总产量", ORANGE)],
     "bullets": ["当阳市是重要农业生产区，稳定灌溉直接关联粮食安全与乡村产业。", "项目覆盖面积约占全市粮食种植面积的一部分，但对三村抗旱稳产意义集中。"],
     "source": "来源：报告3.1.3"},
    {"number": 16, "type": "metrics", "chapter": "第3章 区域背景", "title": "降雨总量不低，但年际与年内错配造成季节性缺水",
     "metrics": [("994.6 mm", "水库多年平均降雨量", TEAL), ("81.7%", "4—10月降雨占比", NAVY), ("4.00 km²", "坝址以上汇水面积", GREEN), ("180 万m³", "多年平均径流量", ORANGE)],
     "bullets": ["作物需水高峰与枯水期叠加，是联合调蓄的根本原因。", "区域地形西北高、东南低，丘岗地占比高，输配水与调蓄工程重要。"],
     "source": "来源：报告3.1.2、3.1.4"},
    {"number": 17, "type": "bars", "chapter": "第3章 区域背景", "title": "2024年水资源总量处于十年低位，抗旱年份更依赖工程调配",
     "values": [("多年平均水资源总量", 7.84, " 亿m³", NAVY), ("2016年", 13.23, " 亿m³", TEAL), ("2020年", 14.61, " 亿m³", GREEN), ("2019年", 2.81, " 亿m³", ORANGE), ("2024年", 2.83, " 亿m³", RED)],
     "note": "报告判断：2024年较多年平均低约52%，与2019年共同构成近十年谷值。",
     "source": "来源：报告3.2.1、表3.2-1"},
    {"number": 18, "type": "cards", "chapter": "第3章 区域背景", "title": "水源本底水质较好，环境风险主要来自农业面源而非点源",
     "cards": [("玉泉水库上游", "以天然汇水区为主，工业与生活污染干扰较低。", TEAL), ("群利一队断面", "2024年水质达到地表水Ⅱ类标准。", GREEN), ("灌溉适用性", "满足农田灌溉水质标准，可作为合格农业水源。", NAVY), ("主要管理风险", "化肥农药随回归水流失，需源头减量和生态拦截。", ORANGE)],
     "source": "来源：报告3.2.2、5.2.6、7.1"},
    {"number": 19, "type": "flow", "chapter": "第3章 区域背景", "title": "当阳市已形成“蓄、引、提”结合的多水源供水体系",
     "items": [("蓄水工程", "128座水库，2024年供水1.648亿m³", NAVY), ("引水工程", "百里长渠、五七长渠及跨区干渠", TEAL), ("提水工程", "40座泵站，总设计流量19.58m³/s", GREEN), ("联合配置", "地表水供水占主导，干渠承担跨区补源", ORANGE)],
     "note": "2024年总供水量3.444亿m³，其中地表水3.349亿m³。",
     "source": "来源：报告3.3.1"},
    {"number": 20, "type": "bars", "chapter": "第3章 区域背景", "title": "农业占全市用水量近四分之三，是节水与配置优化的主战场",
     "values": [("农业用水", 2.550, " 亿m³", GREEN), ("生活用水", 0.538, " 亿m³", TEAL), ("工业用水", 0.356, " 亿m³", ORANGE)],
     "note": "农业占74.06%；人均综合用水量822m³、农田亩均386m³，均高于宜昌市平均水平。",
     "source": "来源：报告3.3.2"},
    {"number": 21, "type": "cards", "chapter": "第3章 区域背景", "title": "四类约束决定新增取水必须依靠节水和跨源调度",
     "cards": [("开发程度偏高", "近十年平均开发利用程度43.03%，高于宜昌市15.15%。", RED), ("用水效率不均", "人均、亩均和万元GDP用水量仍有下降空间。", ORANGE), ("季节性缺水", "雨量时空分布与作物需水峰值错配。", TEAL), ("面源保护压力", "农业退水与养殖污染对水源保护形成持续压力。", GREEN)],
     "source": "来源：报告3.3.3、3.4.2"},
    {"number": 22, "type": "metrics", "chapter": "第3章 区域背景", "title": "总量指标尚未超限，但静态余量不足以直接覆盖申请量",
     "metrics": [("3.5000 亿m³", "2024年总量控制指标", NAVY), ("3.4437 亿m³", "2024年实际用水总量", TEAL), ("98.39%", "指标占用率", ORANGE), ("563 万m³", "静态剩余量", RED)],
     "bullets": ["750 万m³申请量高于静态余量187 万m³。", "许可阶段需落实外调水量分配、年度计划与总量指标统筹，不能仅以“未超指标”作为充分条件。"],
     "source": "来源：报告3.4.1；静态余量为计算值"},
    {"number": 23, "type": "divider", "chapter_no": "04", "title": "用水合理性分析", "subtitle": "从历史用水、作物结构、灌溉定额、供需平衡和节水潜力，核定750万m³申请量。"},
    {"number": 24, "type": "flow", "chapter": "第4章 用水合理性", "title": "供水服务通过“引—蓄—输—配—灌”五个环节完成",
     "items": [("引水", "东风三干渠按缺水过程补源", TEAL), ("调蓄", "玉泉水库平衡月度来水与需水", NAVY), ("输水", "T200及干支渠防渗输送", GREEN), ("配水", "节制闸、剅闸、量水堰精细控制", ORANGE), ("灌溉", "按作物生育期与墒情供水", RED)],
     "source": "来源：报告4.1.1—4.1.2"},
    {"number": 25, "type": "bars", "chapter": "第4章 用水合理性", "title": "枯水年需求明显抬升，2024年毛灌溉用水量达到三年峰值",
     "values": [("2023 平水年", 810.90, " 万m³", TEAL), ("2024 枯水年", 901.31, " 万m³", RED), ("2025 平水年", 817.70, " 万m³", GREEN)],
     "note": "对应年降雨量分别为800.5、542.0、820.0mm；气候波动是年度用水变化的首要因素。",
     "source": "来源：报告表4.1-1"},
    {"number": 26, "type": "metrics", "chapter": "第4章 用水合理性", "title": "既有工程已具备计量、闸控和骨干输水基础",
     "metrics": [("1,480 m", "T200灌排渠整治长度", TEAL), ("2 座", "重建节制闸", NAVY), ("7 处", "重建剅闸", GREEN), ("25 处", "精准计量与信息化设施", ORANGE)],
     "bullets": ["另建量水堰4处，东风三干渠和玉泉渠已实施闸门远程智能控制。", "下一步重点由“有设施”转向“数据闭环、维护校验和调度模型应用”。"],
     "source": "来源：报告4.1.2"},
    {"number": 27, "type": "cards", "chapter": "第4章 用水合理性", "title": "节水路径覆盖工程、农艺、灌水技术与价格管理",
     "cards": [("渠系防渗", "U形渠、砼护底、低压管道降低渗漏与蒸发。", TEAL), ("农艺节水", "旱育秧、深耕密植、调整种植季节与保墒。", GREEN), ("分类灌溉", "畦灌、沟灌、喷微灌、滴灌和水肥一体化。", ORANGE), ("水稻控灌", "薄、浅、湿、晒模式，报告称亩均可节水约100m³。", NAVY), ("管理节水", "按方收费、超定额累进加价、用水户参与管护。", RED)],
     "source": "来源：报告4.1.3"},
    {"number": 28, "type": "cards", "chapter": "第4章 用水合理性", "title": "规划水平年维持现有作物结构，需水核算不依赖扩种假设",
     "cards": [("中稻", "主要高耗水作物，是需水量的主导项。", NAVY), ("油菜", "旱作物，采用75%水文年定额延用至90%。", TEAL), ("小麦", "种植规模维持现状，定额按先进值核算。", GREEN), ("玉米", "面积占比较低，采用渠道防渗灌溉定额。", ORANGE)],
     "source": "来源：报告4.2.1、表4.2-1"},
    {"number": 29, "type": "bars", "chapter": "第4章 用水合理性", "title": "P=90%条件下，中稻定额显著高于其他作物",
     "values": [("中稻", 584, " m³/亩·年", NAVY), ("玉米", 134, " m³/亩·年", ORANGE), ("油菜", 87, " m³/亩·年", TEAL), ("小麦", 66, " m³/亩·年", GREEN)],
     "note": "灌溉设计保证率取90%；油菜、小麦、玉米缺少90%定额时，报告沿用75%水文年值。",
     "source": "来源：报告表4.2-2"},
    {"number": 30, "type": "flow", "chapter": "第4章 用水合理性", "title": "需水量由种植面积、作物定额和灌溉利用系数共同决定",
     "items": [("种植规模", "三村农田总面积17,621.55亩", NAVY), ("作物定额", "按湖北省农业用水定额先进值", TEAL), ("利用系数", "规划水平年目标0.650", GREEN), ("毛需水量", "各作物净需水量除以利用系数", ORANGE)],
     "note": "报告正文存在若干缺数，正式汇报应以表4.2-3最终签章数据替换；本稿不对缺失值作推测。",
     "source": "来源：报告4.2.1、表4.2-3"},
    {"number": 31, "type": "cards", "chapter": "第4章 用水合理性", "title": "水库来水核算必须同时扣除生态流量并匹配特枯典型年",
     "cards": [("频率分析", "设置P=50%、75%、90%三个设计情景。", NAVY), ("参证资料", "采用距水库约11km的2007—2025年逐月雨量资料。", TEAL), ("生态约束", "按Tennant法预留多年平均径流量的10%。", GREEN), ("可供水量", "设计径流量扣除生态下泄后，才可进入灌溉供水。", ORANGE)],
     "source": "来源：报告4.2.2、5.2.3—5.2.4"},
    {"number": 32, "type": "metrics", "chapter": "第4章 用水合理性", "title": "报告采用的一组闭合口径显示，本地水源仅承担约13%的年供水",
     "metrics": [("112.57 万m³", "P=90%设计径流量", NAVY), ("18.00 万m³", "生态下泄量", GREEN), ("94.57 万m³", "本地净可供水量", TEAL), ("12.6%", "本地水源占750万m³", ORANGE)],
     "bullets": ["上述口径与报告另一幅图中的75.33/14.74/60.59万m³不一致。", "正式报批前必须统一设计径流、生态流量及可供水量表格。"],
     "source": "来源：报告水平衡图；存在口径冲突"},
    {"number": 33, "type": "flow", "chapter": "第4章 用水合理性", "title": "655.43万m³外调补源是实现90%保证率的关键条件",
     "items": [("本地净供水", "玉泉水库94.57万m³", TEAL), ("外调补源", "东风三干渠655.43万m³", ORANGE), ("联合供水", "合计750.00万m³", NAVY)],
     "note": "外调水占比约87.4%；引水协议、年度分配和高峰期输水能力是许可的前置条件。",
     "source": "来源：报告4.2、5.2；采用闭合口径94.57+655.43"},
    {"number": 34, "type": "bars", "chapter": "第4章 用水合理性", "title": "灌溉需水高度集中于5—8月，7月是全年调度峰值",
     "values": [("5月", 123.75, " 万m³", TEAL), ("6月", 93.75, " 万m³", GREEN), ("7月", 217.50, " 万m³", RED), ("8月", 153.75, " 万m³", ORANGE), ("9月", 30.00, " 万m³", NAVY)],
     "note": "7—8月合计371.25万m³，占全年49.5%；联合调度应围绕高峰期预蓄、错峰引水和库容安全展开。",
     "source": "来源：报告表4.2规划水平年耗水及退水量"},
    {"number": 35, "type": "flow", "chapter": "第4章 用水合理性", "title": "750万m³取水最终形成600万m³耗水和150万m³回归水",
     "items": [("联合取水", "750.00万m³进入灌区", NAVY), ("农业耗水", "600.00万m³，占80%", GREEN), ("回归退水", "150.00万m³，占20%", TEAL)],
     "note": "回归水通过田间沟渠、地表漫流和土壤下渗，分散进入浅层地下水或周边地表水体。",
     "source": "来源：报告4.2.3、7.1"},
    {"number": 36, "type": "bars", "chapter": "第4章 用水合理性", "title": "规划利用系数0.650高于现有对标值，但实现依赖持续改造",
     "values": [("湖北省平均", 0.528, "", GREEN), ("长江流域平均", 0.547, "", TEAL), ("全国平均", 0.580, "", NAVY), ("规划目标", 0.650, "", ORANGE)],
     "note": "报告指出渠道淤积、衬砌不足、设施老化和监测薄弱仍制约节水效益。",
     "source": "来源：报告4.3"},
    {"number": 37, "type": "matrix", "chapter": "第4章 用水合理性", "title": "用水核定结论成立，但需把三项数据条件写入许可约束",
     "headers": ["核定事项", "报告结论", "关键依据", "许可约束"],
     "rows": [("年取水量", "750.00万m³", "规划需水与联合供水", "不得超计划、超定额"),
              ("水源结构", "水库+三干渠", "本地来水不足", "落实引水协议和年度水量"),
              ("年耗水量", "600.00万m³", "80%耗水系数", "开展水平衡复核"),
              ("年退水量", "150.00万m³", "20%回归系数", "监测面源污染和退水峰值"),
              ("总量指标", "报告判断符合", "2024年未超控制线", "明确750万m³指标统筹来源")],
     "source": "来源：报告4.4；总量约束为审查提示"},
    {"number": 38, "type": "divider", "chapter_no": "05", "title": "取水水源论证", "subtitle": "验证联合水源方案的唯一性、资料基础、供水能力、水质和工程运行可靠性。"},
    {"number": 39, "type": "cards", "chapter": "第5章 取水水源", "title": "现有联合水源最契合历史用水路径，另设水源方案缺乏必要性",
     "cards": [("本地水源", "玉泉水库长期承担本灌区农业供水，工程体系成熟。", NAVY), ("补充水源", "东风三干渠具备跨区域农业输水功能。", TEAL), ("空间匹配", "水源、取水口、渠系与三村灌区紧密衔接。", GREEN), ("方案判断", "优先利用本地地表水，缺口由既有干渠补充。", ORANGE)],
     "source": "来源：报告5.1"},
    {"number": 40, "type": "flow", "chapter": "第5章 取水水源", "title": "可靠性论证以长序列降雨、工程特性和月度调度演算为主线",
     "items": [("资料输入", "2007—2025逐月雨量、除险加固工程特性", NAVY), ("来水分析", "频率计算与P=90%典型年径流", TEAL), ("供需演算", "生态流量、灌溉过程与三干渠补水", GREEN), ("安全校核", "死库容、设计洪水位库容和月末库容", ORANGE)],
     "source": "来源：报告5.2.1—5.2.5"},
    {"number": 41, "type": "metrics", "chapter": "第5章 取水水源", "title": "联合调度同时受供水、生态和防洪三条边界约束",
     "metrics": [("6.4 万m³", "死库容下限", RED), ("225 万m³", "正常蓄水位库容", TEAL), ("248.48 万m³", "设计洪水位库容上限", NAVY), ("7—8月", "重点错峰调度期", ORANGE)],
     "bullets": ["最低库容不得跌破死库容，避免破坏供水和水生生境。", "最高库容不得超过设计洪水位库容，兼顾汛期防洪安全。", "三干渠补水应按月度缺水过程落实，不仅核定年度总量。"],
     "source": "来源：报告4.2.2、5.2.5、5.2.8"},
    {"number": 42, "type": "image", "chapter": "第5章 取水水源", "title": "取水口布局和水质条件均具备工程可实施性",
     "image": "image25.png",
     "bullets": [("水质可靠", "群利一队断面Ⅱ类，满足农业灌溉要求", GREEN), ("工程成熟", "闸渠、量水堰和远程控制设施已建设", TEAL), ("位置合理", "靠近灌区核心需水区并衔接三干渠", ORANGE)],
     "source": "来源：报告5.2.6—5.2.8、附图六"},
    {"number": 43, "type": "cards", "chapter": "第6章 取水影响", "title": "取水影响总体可控，但前提是生态下泄和外调水计划刚性执行",
     "cards": [("区域水资源", "联合补源降低对本地径流的挤占，年度配置影响有限。", TEAL), ("水库生态", "库容保持死库容以上，维持最小生境空间。", GREEN), ("下游生态", "生态流量优先下泄，避免枯水期断流。", NAVY), ("水功能区", "项目无生产生活废污水，不改变水质目标。", ORANGE), ("其他用户", "水库无城镇工业用户；干渠沿线权益需按协议保障。", RED)],
     "source": "来源：报告第6章"},
    {"number": 44, "type": "flow", "chapter": "第7章 退水影响", "title": "退水属于分散农业回归水，不形成集中排污口",
     "items": [("田间渗漏", "灌溉水向土壤剖面下渗", TEAL), ("灌溉尾水", "沿田间沟渠和坡面漫流", NAVY), ("生态净化", "土壤吸附、沟渠沉淀和植被拦截", GREEN), ("受纳路径", "浅层地下水、玉泉河及小微水体", ORANGE)],
     "note": "退水高峰与7—8月灌溉高峰同步，空间上呈大面积、多散点分布。",
     "source": "来源：报告7.1"},
    {"number": 45, "type": "matrix", "chapter": "第7章 退水影响", "title": "退水方案合理性来自规模、路径和环境风险三方面",
     "headers": ["评价维度", "主要判断", "风险点", "控制要求"],
     "rows": [("退水规模", "150万m³/年，回归系数20%", "系数为类比值", "运行后开展水平衡复核"),
              ("排放路径", "分散下渗与沟渠汇流", "雨季短时冲刷", "保留生态沟渠与拦截带"),
              ("水功能区", "不改变农业用水区功能", "氮磷累积", "监测TN、TP、COD等指标"),
              ("水生态", "回补地下水与小微水体", "富营养化", "化肥农药减量增效"),
              ("第三方", "无敏感集中用水户", "异常水质事件", "建立预警与应急响应")],
     "source": "来源：报告7.2—7.5"},
    {"number": 46, "type": "cards", "chapter": "第8章 节约保护管理", "title": "工程措施只有进入制度、数据和运维闭环，才能持续兑现节水效益",
     "cards": [("节约", "渠道防渗、低压管输、喷微灌、水肥一体化。", TEAL), ("保护", "测土配方、化肥农药减量、生态农业与联防机制。", GREEN), ("许可计划", "按批复规模、用途和年度计划开展取水。", NAVY), ("计量监测", "取水实时计量、台账上报、设备校验和水平衡测试。", ORANGE), ("工程运维", "落实人员经费，巡查水库、渠系、闸门和信息设施。", RED), ("生态管理", "水质水量常态监测，异常启动应急响应。", TEAL)],
     "source": "来源：报告第8章"},
    {"number": 47, "type": "matrix", "chapter": "第9章 结论建议", "title": "报告总体结论为可行，但可靠性具有明确的条件性",
     "headers": ["论证主题", "报告结论", "成立条件", "审查关注"],
     "rows": [("用水合理性", "750万m³规模合理", "定额与规划需水闭合", "补齐表4.2-3缺失数字"),
              ("水源可靠性", "联合水源可保障P=90%", "三干渠补水按月落实", "统一两组供水计算口径"),
              ("取水影响", "总体可控", "生态流量和库容红线", "干渠其他用户权益"),
              ("退水影响", "方案可行", "面源减量与生态拦截", "运行期水质监测"),
              ("管理能力", "具备工程基础", "计量、台账、维护、预警", "形成责任与考核闭环")],
     "source": "来源：报告9.1"},
    {"number": 48, "type": "cards", "chapter": "第9章 结论建议", "title": "建议将五项前置条件写入许可与后续实施要求",
     "cards": [("统一计算口径", "复核设计径流、生态流量、本地可供水量和外调补水量。", RED), ("落实水量指标", "明确750万m³总量指标来源及年度计划统筹方式。", ORANGE), ("签订引水协议", "明确三干渠月度流量、时段、调度优先级和违约处置。", TEAL), ("完善监测闭环", "覆盖取水、配水、库容、退水和关键水质断面。", GREEN), ("强化设施管护", "推进末级渠系防渗、设备校验和长效运维经费。", NAVY)],
     "source": "来源：报告9.2；结合报告数据质量审查"},
    {"number": 49, "type": "divider", "chapter_no": "END", "title": "请专家审议", "subtitle": "核心审查问题：水量口径是否统一、外调补源是否落实、总量指标是否有出处、监测管理是否可执行。"},
]


def render(slide):
    return {
        "cover": make_cover,
        "divider": make_divider,
        "agenda": make_agenda,
        "metrics": make_metrics,
        "cards": make_cards,
        "bars": make_bars,
        "flow": make_flow,
        "image": make_image,
        "matrix": make_matrix,
    }[slide["type"]](slide)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.svg"):
        old.unlink()
    plan = []
    for slide in SLIDES:
        name = f"{slide['number']:02d}_{slide['type']}.svg"
        (OUT / name).write_text(render(slide), encoding="utf-8")
        plan.append(
            {
                "page": slide["number"],
                "type": slide["type"],
                "chapter": slide.get("chapter", f"Chapter {slide.get('chapter_no', '')}"),
                "title": slide["title"],
                "source": slide.get("source", ""),
            }
        )
    plan_path = OUT.parent / "slide-plan.json"
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"slides": len(SLIDES), "svg_dir": str(OUT), "plan": str(plan_path)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
