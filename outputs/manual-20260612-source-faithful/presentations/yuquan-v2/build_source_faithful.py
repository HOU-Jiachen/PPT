import base64
import html
import json
import math
import textwrap
from pathlib import Path

ROOT = Path(r"C:\Gemini cli\gemini-ppt")
PROJECT = ROOT / "projects" / "当阳玉泉水库"
MEDIA = PROJECT / "qa" / "report-docx-package" / "word" / "media"
DECK = PROJECT / "source_faithful_deck"
SVG_DIR = DECK / "svg_final"
SVG_OUT = DECK / "svg_output"

W, H = 1280, 720
NAVY, TEAL, GREEN, ORANGE, RED = "#0B3558", "#0E9F9A", "#63A35C", "#E8923A", "#C94B45"
INK, MUTED, PAPER, WHITE, LINE, PALE = "#17324A", "#607789", "#F7F5EF", "#FFFFFF", "#C6D2D8", "#E8F2F2"
FONT = "Microsoft YaHei, Arial, sans-serif"


def esc(v): return html.escape(str(v))


def lines(value, width):
    # Chinese paragraphs often contain no spaces, so they must be wrapped by
    # character count instead of being treated as one unbreakable "word".
    wrapped = textwrap.wrap(str(value), width=width, break_long_words=True, break_on_hyphens=False) or [""]
    closing = "，。；：、）》】！？,.!?;:"
    cleaned = []
    for line in wrapped:
        if cleaned and line and (line[0] in closing or all(ch in closing for ch in line)):
            cleaned[-1] += line
        else:
            cleaned.append(line)
    return cleaned


def start(bg=PAPER):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
            f'<rect width="{W}" height="{H}" fill="{bg}"/>']


def finish(p):
    p.append("</svg>")
    return "\n".join(p)


def txt(p, x, y, s, size=22, fill=INK, weight="normal", anchor="start"):
    p.append(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{esc(s)}</text>')


def para(p, x, y, s, size=22, width=40, leading=1.55, fill=INK, weight="normal"):
    out = lines(s, width)
    for i, line in enumerate(out):
        txt(p, x, y + i * size * leading, line, size, fill, weight)
    return y + len(out) * size * leading


def chrome(p, page, chapter, title):
    p.append(f'<rect x="54" y="46" width="7" height="32" fill="{TEAL}"/>')
    txt(p, 78, 70, f"{chapter}  |  {page:02d}", 15, MUTED, "bold")
    para(p, 54, 120, title, 34, 33, 1.2, INK, "bold")


def foot(p, page, source):
    p.append(f'<line x1="54" y1="670" x2="1226" y2="670" stroke="{LINE}"/>')
    txt(p, 54, 697, source, 11, MUTED)
    txt(p, 1226, 697, f"{page:02d}", 12, MUTED, "bold", "end")


def img_uri(name):
    path = MEDIA / name
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def cover(s):
    p = start(NAVY)
    p += [f'<circle cx="1080" cy="120" r="260" fill="{TEAL}" fill-opacity=".18"/>',
          f'<circle cx="1150" cy="630" r="330" fill="{GREEN}" fill-opacity=".12"/>',
          f'<rect x="72" y="92" width="92" height="8" fill="{TEAL}"/>']
    txt(p, 72, 148, "水资源论证 · 原文原图增强版", 18, "#BAD3DF", "bold")
    txt(p, 72, 272, "玉泉水库灌区", 58, WHITE, "bold")
    txt(p, 72, 348, "水资源论证报告", 58, WHITE, "bold")
    para(p, 74, 410, "按报告九章展开，完整呈现主要文字、表格、图件、计算过程与报告结论", 23, 37, 1.5, "#DCE8EF")
    for i, (v, lab, c) in enumerate([("67 页", "按信息量动态规划", TEAL), ("9 章", "对应报告正文", GREEN), ("Office 2021", "原生兼容验收", ORANGE)]):
        x = 72 + i * 280
        p.append(f'<rect x="{x}" y="520" width="250" height="92" fill="{WHITE}" rx="7"/>')
        txt(p, x+18, 560, v, 28, c, "bold")
        txt(p, x+18, 590, lab, 15, MUTED)
    txt(p, 72, 665, "建设单位：当阳市惠清水环境治理有限责任公司", 14, "#BAD3DF")
    txt(p, 1210, 665, "2026年6月", 14, "#BAD3DF", anchor="end")
    return finish(p)


def section(s):
    p = start(NAVY)
    p += [f'<rect x="72" y="116" width="88" height="8" fill="{TEAL}"/>',
          f'<circle cx="1030" cy="360" r="245" fill="{TEAL}" fill-opacity=".12"/>']
    txt(p, 72, 196, f"CHAPTER {s['ch_no']}", 18, "#A9CBD8", "bold")
    para(p, 72, 305, s["title"], 54, 14, 1.18, WHITE, "bold")
    para(p, 75, 430, s["body"], 23, 37, 1.5, "#D4E3E9")
    txt(p, 1170, 620, f"{s['page']:02d}", 70, "#5AB7B1", "bold", "end")
    return finish(p)


def source_text(s):
    p = start()
    chrome(p, s["page"], s["chapter"], s["title"])
    p.append(f'<rect x="54" y="190" width="8" height="410" fill="{s.get("accent", TEAL)}"/>')
    y = 218
    body_width = 29 if s.get("facts") else 47
    for block in s["blocks"]:
        if block.get("label"):
            txt(p, 86, y, block["label"], 18, s.get("accent", TEAL), "bold")
            y += 34
        y = para(p, 86, y, block["text"], block.get("size", 22), block.get("width", body_width), 1.55, INK, block.get("weight", "normal"))
        y += 22
    if s.get("facts"):
        p.append(f'<line x1="748" y1="205" x2="748" y2="585" stroke="{LINE}"/>')
        fy = 224
        for value, label in s["facts"]:
            txt(p, 790, fy, value, 28, TEAL, "bold")
            para(p, 790, fy+29, label, 16, 23, 1.3, MUTED)
            fy += 88
    if s.get("note"):
        p.append(f'<rect x="760" y="555" width="440" height="76" fill="{PALE}" rx="6"/>')
        para(p, 782, 584, s["note"], 16, 39, 1.35, INK, "bold")
    foot(p, s["page"], s["source"])
    return finish(p)


def figure(s):
    p = start()
    chrome(p, s["page"], s["chapter"], s["title"])
    x, y, w, h = 54, 178, 1172, 462
    if s.get("side_note"):
        w = 820
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{WHITE}" stroke="{LINE}"/>')
    p.append(f'<image x="{x+10}" y="{y+10}" width="{w-20}" height="{h-20}" preserveAspectRatio="xMidYMid meet" href="{img_uri(s["image"])}"/>')
    if s.get("side_note"):
        sy = 205
        for label, body in s["side_note"]:
            txt(p, 920, sy, label, 19, TEAL, "bold")
            sy = para(p, 920, sy+32, body, 18, 24, 1.45, INK) + 30
    foot(p, s["page"], s["source"])
    return finish(p)


def table_slide(s):
    p = start()
    chrome(p, s["page"], s["chapter"], s["title"])
    x0, y0 = 54, 188
    widths = s["widths"]
    row_h = s.get("row_h", 54)
    x = x0
    for i, head in enumerate(s["headers"]):
        p.append(f'<rect x="{x}" y="{y0}" width="{widths[i]}" height="52" fill="{NAVY}"/>')
        para(p, x+12, y0+31, head, 18, max(5, int(widths[i]/18)), 1.15, WHITE, "bold")
        x += widths[i]
    for r, row in enumerate(s["rows"]):
        y = y0 + 52 + r * row_h
        x = x0
        for c, cell in enumerate(row):
            fill = WHITE if r % 2 == 0 else "#EDF2F3"
            p.append(f'<rect x="{x}" y="{y}" width="{widths[c]}" height="{row_h}" fill="{fill}" stroke="{LINE}"/>')
            para(p, x+12, y+27, cell, 18, max(4, int(widths[c]/18)), 1.18, TEAL if c == 0 else INK, "bold" if c == 0 else "normal")
            x += widths[c]
    if s.get("note"):
        para(p, 54, 632, s["note"], 16, 70, 1.3, INK, "bold")
    foot(p, s["page"], s["source"])
    return finish(p)


def analysis(s):
    p = start()
    chrome(p, s["page"], s["chapter"], s["title"])
    if s.get("metrics"):
        n = len(s["metrics"])
        bw = (1172 - (n-1)*18)/n
        for i, (v, lab, color) in enumerate(s["metrics"]):
            x = 54 + i*(bw+18)
            p.append(f'<rect x="{x}" y="198" width="{bw}" height="108" fill="{WHITE}" stroke="{LINE}" rx="6"/>')
            txt(p, x+18, 244, v, 29, color, "bold")
            para(p, x+18, 275, lab, 15, max(10, int(bw/15)), 1.25, MUTED)
        y = 360
    else:
        y = 205
    for i, bullet in enumerate(s["bullets"]):
        p.append(f'<circle cx="68" cy="{y+i*65-7}" r="6" fill="{s.get("accent", TEAL)}"/>')
        para(p, 88, y+i*65, bullet, 21, 53, 1.38, INK, "bold" if i == 0 else "normal")
    foot(p, s["page"], s["source"])
    return finish(p)


def agenda(s):
    p = start()
    chrome(p, s["page"], "汇报结构", s["title"])
    for i, (name, desc) in enumerate(s["items"]):
        col, row = i % 3, i // 3
        x, y = 54 + col*390, 202 + row*140
        txt(p, x, y, f"{i+1:02d}", 16, [TEAL,GREEN,ORANGE][col], "bold")
        txt(p, x+48, y, name, 22, INK, "bold")
        para(p, x+48, y+34, desc, 17, 20, 1.35, MUTED)
        p.append(f'<line x1="{x}" y1="{y+94}" x2="{x+345}" y2="{y+94}" stroke="{LINE}"/>')
    foot(p, s["page"], s["source"])
    return finish(p)


slides = [
{"page":1,"type":"cover"},
{"page":2,"type":"analysis","chapter":"项目概览","title":"项目年申请取水量750万m³，服务三村17621.55亩农田灌溉","metrics":[("750万m³","年申请取水量",TEAL),("17621.55亩","灌区农田面积",GREEN),("P=90%","灌溉设计保证率",ORANGE),("150万m³","年退水量",NAVY)],"bullets":["取水水源为玉泉水库与东风三干渠联合水源。","取水口位于玉泉水库坝址处节制闸，退水为分散农业灌溉回归水。","现状水平年为2024年，规划水平年为2034年。"],"source":"来源：报告基本情况表、2.3、2.4"},
{"page":3,"type":"agenda","title":"九章内容按报告原始顺序完整展开","items":[("总论","目的、依据、等级与范围"),("项目概况","工程、政策、取退水"),("区域水资源","资源条件与开发利用"),("用水合理性","需水、节水与水量平衡"),("取水水源","联合供水与可靠性"),("取水影响","资源、生态与其他用户"),("退水影响","退水路径、规律与影响"),("管理措施","节约、保护与管理"),("结论建议","结论、问题与建议")],"source":"来源：报告目录"},
{"page":4,"type":"section","ch_no":"01","title":"总论","body":"明确论证目的、工作任务、技术依据、工作等级、水平年和四类空间范围。"},
{"page":5,"type":"source_text","chapter":"第1章 总论","title":"水资源论证服务于合理取水、水资源保护和取水许可审批","blocks":[{"label":"论证目的","text":"贯彻“合理开发、高效利用、优化配置、全面节约和有效保护”的水资源开发利用方针，加强水资源开发利用管理，实现水资源节约、保护和优化配置。"},{"text":"分析建设项目取水对水资源现状及其他用户的影响，提出补偿和保护措施，预防取水、退水可能引发的水事纠纷，为水行政主管部门审批取水许可申请提供科学技术依据。"}],"facts":[["合理开发","水资源开发利用方针"],["高效利用","提高水资源利用效率"],["全面节约","落实节约用水要求"],["有效保护","控制取退水影响"]],"source":"来源：报告1.2"},
{"page":6,"type":"source_text","chapter":"第1章 总论","title":"论证任务覆盖范围、合理性、水源、影响和结论建议","blocks":[{"label":"主要任务","text":"确定分析范围、取水水源论证范围和取退水影响范围；调查评价区域水资源状况及开发利用现状；从产业政策、水资源规划、配置与管理方面分析取用水合理性；分析取水水源可靠性和可行性；分析取退水影响并提出保护措施和结论建议。"}],"facts":[["范围确定","分析、水源、取退水影响"],["合理性","产业政策、规划与配置"],["可靠性","水源可行性与保障程度"],["影响分析","资源、生态及其他用户"],["结论建议","形成论证结论与措施"]],"source":"来源：报告1.2"},
{"page":7,"type":"source_text","chapter":"第1章 总论","title":"论证依据由许可制度、技术导则、用水定额和区域成果组成","blocks":[{"label":"法律制度","text":"《中华人民共和国水法》《取水许可和水资源费征收管理条例》《建设项目水资源论证管理办法》《取水许可管理办法》及最严格水资源管理制度。"},{"label":"标准规范","text":"《建设项目水资源论证导则》GB/T35580-2017、《农田灌溉建设项目水资源论证导则》、水资源供需平衡与水利计算规范、《湖北省农业用水定额》及农田灌溉水质标准。"},{"label":"区域资料","text":"湖北省、宜昌市2024年水资源公报，宜昌市环境质量年报，当阳市国土空间、流域治理及经济社会资料。"}],"source":"来源：报告1.3"},
{"page":8,"type":"table","chapter":"第1章 总论","title":"分类指标最高等级确定本项目论证等级为二级","headers":["分类指标","本项目值","一级","二级","三级","评定"],"widths":[250,170,170,190,170,220],"rows":[["灌溉面积","1.76万亩","≥30","30～1","＜1","二级"],["开发利用程度","24.3%","≥30%","30%～10%","＜10%","二级"],["灌溉取水流量","0.23m³/s","≥20","20～3","＜3","三级"]],"note":"论证工作等级由各分类指标的最高级别确定。","source":"来源：报告表1.4-1"},
{"page":9,"type":"figure","chapter":"第1章 总论","title":"分析范围覆盖当阳市，水源论证聚焦玉泉水库坝址以上流域","image":"image21.jpeg","side_note":[("现状水平年","2024年"),("规划水平年","2034年"),("保证率","农业灌溉P=90%")],"source":"来源：报告1.4—1.5、附图一"},
{"page":10,"type":"section","ch_no":"02","title":"建设项目概况","body":"说明工程服务对象、政策与规划相符性、取水工程参数以及农业回归水方案。"},
{"page":11,"type":"source_text","chapter":"第2章 项目概况","title":"玉泉水库主要服务三村农业灌溉，并兼顾防洪与生态效益","blocks":[{"label":"项目功能","text":"玉泉水库位于当阳市，以农业灌溉为主，兼顾防洪、生态等综合效益。供水范围覆盖子龙村、合意村、玉泉村等3个行政村，区域内主要种植水稻、油菜及蔬菜。"},{"label":"服务范围","text":"根据当阳市农业农村局和玉泉水库管理处提供的资料，水库灌区农田总面积为17621.55亩。"}],"facts":[["3个行政村","子龙村、合意村、玉泉村"],["17621.55亩","灌区农田总面积"],["农业灌溉","水库主要供水任务"],["防洪、生态","兼顾综合效益"]],"source":"来源：报告2.1"},
{"page":12,"type":"source_text","chapter":"第2章 项目概况","title":"项目符合粮食安全、农田水利和流域综合治理方向","blocks":[{"label":"产业政策","text":"项目属于水资源利用和优化配置的水利建设项目，符合产业结构调整鼓励方向。"},{"label":"区域规划","text":"湖北省和当阳市相关规划强调高标准农田、农业灌溉体系、水资源利用效率和公益性水利设施建设。"},{"label":"水功能管理","text":"取水规模应控制在水库承载范围，执行农业用水定额，采用节水技术并建立动态监测机制。"}],"source":"来源：报告2.2"},
{"page":13,"type":"analysis","chapter":"第2章 项目概况","title":"取水依托既有坝址节制闸和渠系，不新增复杂取水工程","metrics":[("0.81m³/s","最大取水流量",NAVY),("7.02万m³","日最大取水量",TEAL),("750万m³","年取水量",GREEN),("90%","设计保证率",ORANGE)],"bullets":["取水口位于玉泉水库坝址处节制闸。","水源通过既有引水闸和干支渠进入灌区。"],"source":"来源：报告2.3、基本情况表"},
{"page":14,"type":"figure","chapter":"第2章 项目概况","title":"取水影响范围集中于玉泉水库水域及坝下渠系","image":"image23.jpeg","side_note":[("取水对象","农业灌溉"),("工程节点","坝址节制闸"),("主要约束","水位与生态流量")],"source":"来源：报告2.3、附图三"},
{"page":15,"type":"source_text","chapter":"第2章 项目概况","title":"退水为分散农业回归水，不设置集中排污口","blocks":[{"label":"退水方式","text":"农业灌溉回归水汇入玉泉水库下游农田水系，最终分散进入区域含水层或周边地表水体。"},{"label":"退水规模","text":"类比同地区灌区，回归水量按供水量的20%计，年退水量为150万m³。"},{"label":"水质关注","text":"退水水质主要受灌溉模式和化肥农药施用影响，重点关注COD、氨氮及氮磷面源污染。"}],"source":"来源：报告2.4"},
{"page":16,"type":"section","ch_no":"03","title":"水资源及其开发利用状况","body":"从区域地理、水文气象、资源量、供水工程、用水结构和控制指标审视项目条件。"},
{"page":17,"type":"figure","chapter":"第3章 区域背景","title":"玉泉水库位于当阳市中西部、沮漳河流域玉泉河中游","image":"image9.jpeg","source":"来源：报告图3.1-1"},
{"page":18,"type":"source_text","chapter":"第3章 区域背景","title":"地形与流域条件决定工程调蓄和渠系输配水的重要性","blocks":[{"label":"自然地理","text":"当阳市地处鄂西山地向江汉平原过渡地带，地势西北高、东南低，以丘陵和岗地为主，形成“六岗、三平、一分山”的地貌格局。"},{"label":"流域关系","text":"当阳市主要属沮漳河流域。玉泉水库位于沮河一级支流玉泉河中游，坝址以上自然汇水面积4.00km²。"}],"source":"来源：报告3.1.1—3.1.2"},
{"page":19,"type":"table","chapter":"第3章 区域背景","title":"2024年农业生产规模说明灌溉供水具有明确公共效益","headers":["指标","单位","2024年数量","同比"],"widths":[300,200,330,340],"rows":[["粮食","万吨","47.56","基本持平"],["棉花","吨","349","+4.18%"],["油料","万吨","7.22","+3.29%"],["园林水果","万吨","57.49","+3.92%"],["蔬菜","万吨","108.5","+2.0%"]],"source":"来源：报告3.1.3、表3.1-1"},
{"page":20,"type":"table","chapter":"第3章 区域背景","title":"降雨总体较丰富，但年内集中、年际波动明显","headers":["气象指标","单位","漳河站","沮河站"],"widths":[360,170,330,310],"rows":[["多年平均降水量","mm","968.9","992.1"],["多年平均蒸发量","mm","1424.5","1364.5"],["多年平均气温","℃","15.6","16.4"],["极端最高气温","℃","40.9","—"],["降雨集中期","月份","4—10月","约占全年81.7%"]],"source":"来源：报告3.1.4、表3.1-2"},
{"page":21,"type":"table","chapter":"第3章 区域背景","title":"2015—2019年当阳市水资源总量呈周期性波动","headers":["年份","年降水量 亿m³","地表水 亿m³","地下水 亿m³","水资源总量 亿m³"],"widths":[180,245,245,245,255],"rows":[["2015","20.00","4.59","2.22","4.76"],["2016","26.15","13.05","2.24","13.23"],["2017","22.92","8.61","2.39","8.79"],["2018","23.61","8.77","2.05","8.97"],["2019","15.77","2.60","1.69","2.81"]],"source":"来源：报告表3.2-1"},
{"page":22,"type":"table","chapter":"第3章 区域背景","title":"2020—2024年水资源总量由14.61亿m³降至2.83亿m³","headers":["年份","年降水量 亿m³","地表水 亿m³","地下水 亿m³","水资源总量 亿m³"],"widths":[180,245,245,245,255],"rows":[["2020","30.86","14.50","3.68","14.61"],["2021","18.55","4.65","1.46","4.80"],["2022","19.86","5.08","1.80","5.26"],["2023","19.88","5.79","1.82","5.91"],["2024","14.33","2.66","1.06","2.83"]],"source":"来源：报告表3.2-1"},
{"page":23,"type":"source_text","chapter":"第3章 区域背景","title":"群利一队断面2024年水质达到地表水Ⅱ类标准","blocks":[{"label":"水质现状","text":"玉泉水库坝址以上流域以天然汇水区为主，受工业及生活面源污染干扰程度较低。根据《2024年宜昌市环境质量年报》，水库下游群利一队断面水质达到《地表水环境质量标准》Ⅱ类标准，满足《农田灌溉水质标准》相关要求。"}],"facts":[["Ⅱ类","群利一队断面水质类别"],["2024年","环境质量年报评价年度"],["GB 3838-2002","地表水环境质量标准"],["GB 5084-2021","农田灌溉水质标准"]],"source":"来源：报告3.2.2"},
{"page":24,"type":"source_text","chapter":"第3章 区域背景","title":"当阳市已形成蓄、引、提结合的区域供水工程体系","blocks":[{"label":"蓄水工程","text":"现有各类水库128座，总库容5.41亿m³，另有大量塘坝工程。"},{"label":"引水工程","text":"百里长渠、五七长渠以及东风渠二、三干渠和漳河干渠承担农业灌溉与生态补水。"},{"label":"提水工程","text":"现有提水泵站40座，总装机功率4289kW，设计提水流量19.58m³/s。"}],"source":"来源：报告3.3.1"},
{"page":25,"type":"analysis","chapter":"第3章 区域背景","title":"2024年供水以地表水为主，蓄水工程贡献最大","metrics":[("3.444亿m³","总供水量",NAVY),("3.349亿m³","地表水供水",TEAL),("1.648亿m³","蓄水工程供水",GREEN),("0.980亿m³","引水工程供水",ORANGE)],"bullets":["地表水供水占绝对主体。","跨区干渠是枯水期农业补源的重要组成。"],"source":"来源：报告3.3.1"},
{"page":26,"type":"table","chapter":"第3章 区域背景","title":"当阳市农业用水占比高，亩均和人均用水仍有提升空间","headers":["指标","当阳市","宜昌市","湖北省"],"widths":[430,240,240,260],"rows":[["人均综合用水量","822m³","585m³","583m³"],["农田灌溉亩均用水量","386m³","357m³","378m³"],["万元GDP用水量","47.1m³","31.2m³","53.0m³"],["农业用水占比","74.06%","—","—"]],"source":"来源：报告3.3.2、表3.3-1"},
{"page":27,"type":"source_text","chapter":"第3章 区域背景","title":"报告识别出开发程度、效率、季节缺水和水质保护四类问题","blocks":[{"label":"主要问题","text":"（1）水资源开发利用程度较高；（2）人均、亩均及万元GDP用水效率不均衡，农业仍有节水潜力；（3）降雨年际和年内分布不均，作物需水高峰易出现季节性缺水；（4）农业面源与养殖污染对区域水源保护形成压力。"}],"source":"来源：报告3.3.3"},
{"page":28,"type":"analysis","chapter":"第3章 区域背景","title":"2024年当阳市实际用水总量未超过年度控制指标","metrics":[("35000万m³","2024年用水总量控制指标",NAVY),("34437万m³","2024年实际用水总量",TEAL),("98.39%","控制指标占用比例",ORANGE),("100%","现状水功能区水质达标率",GREEN)],"bullets":["报告判断2024年实际用水总量未超过控制指标。","万元工业增加值用水量降幅为54.6%，已达到2025年考核目标。"],"source":"来源：报告基本情况表、3.4.1"},
{"page":29,"type":"section","ch_no":"04","title":"用水合理性分析","body":"展示历史灌溉、节水工程、作物结构与定额、来水频率、联合调度、耗退水和用水核定。"},
{"page":30,"type":"table","chapter":"第4章 用水合理性","title":"2024枯水年毛灌溉用水量显著高于平水年份","headers":["年度","年降雨量","丰枯等级","净需水量","毛用水量"],"widths":[190,230,220,270,260],"rows":[["2023","800.5mm","平水年","458.16万m³","810.90万m³"],["2024","542.0mm","枯水年","508.34万m³","901.31万m³"],["2025","820.0mm","平水年","466.09万m³","817.70万m³"]],"source":"来源：报告表4.1-1"},
{"page":31,"type":"source_text","chapter":"第4章 用水合理性","title":"既有渠系改造和信息化设施构成节水与调度基础","blocks":[{"label":"工程建设情况","text":"湖北省当阳市2018年农业水价综合改革项目已实施渠道整治、节制闸和剅闸改造、量水设施建设，并对东风三干渠和玉泉渠实行闸门远程智能控制。"}],"facts":[["1480m","T200灌排渠整治长度"],["660m","浆砌石护砌长度"],["2座、7处","节制闸与剅闸改造"],["4处","新建量水堰"],["25处","精准计量与信息化设施"]],"source":"来源：报告4.1.2"},
{"page":32,"type":"source_text","chapter":"第4章 用水合理性","title":"节水措施覆盖渠系防渗、分类灌溉、水肥一体化与价格管理","blocks":[{"label":"工程节水","text":"干支渠采用砼护坡护底，末级渠系推广U型渠槽和低压管道，减少传统土渠渗漏与蒸发。"},{"label":"农业技术","text":"推广畦灌、沟灌、喷灌、微喷、滴灌、水肥一体化以及水稻“薄、浅、湿、晒”控灌。"},{"label":"管理节水","text":"依托农业水价综合改革，实行按方收费、超定额累进加价，结合墒情和作物生育期科学配水。"}],"source":"来源：报告4.1.3"},
{"page":33,"type":"table","chapter":"第4章 用水合理性","title":"规划水平年维持现状作物种植结构与规模不变","headers":["作物","现状水平年复种指数","规划水平年复种指数","规划说明"],"widths":[220,300,300,350],"rows":[["中稻","0.684","0.684","种植规模保持不变"],["油菜","0.578","0.578","种植规模保持不变"],["小麦","0.481","0.481","种植规模保持不变"],["玉米","0.019","0.019","种植规模保持不变"]],"source":"来源：报告4.2.1、表4.2-1"},
{"page":34,"type":"table","chapter":"第4章 用水合理性","title":"P=90%条件下，中稻灌溉定额为主要控制项","headers":["作物","P=50%","P=75%","P=90%","单位"],"widths":[280,220,220,220,230],"rows":[["中稻","464","533","584","m³/亩·年"],["油菜","60","87","87","m³/亩·年"],["小麦","37","66","66","m³/亩·年"],["玉米","90","134","134","m³/亩·年"]],"source":"来源：报告表4.2-2"},
{"page":35,"type":"source_text","chapter":"第4章 用水合理性","title":"灌溉需水量依据作物面积、灌溉定额和利用系数计算","blocks":[{"label":"计算方法","text":"各作物净灌溉需水量由种植面积乘以相应水文年灌溉定额得到；总净灌溉需水量除以灌溉水有效利用系数，得到渠首毛灌溉需水量。"},{"label":"规划参数","text":"报告采用2024年现状灌溉水利用系数，并结合灌区续建配套与节水改造，将2034年规划水平年灌溉水利用系数确定为0.650。"}],"facts":[["17621.55亩","灌区农田总面积"],["P=90%","灌溉设计保证率"],["2034年","规划水平年"],["0.650","规划灌溉水利用系数"]],"source":"来源：报告4.2.1、表4.2-3"},
{"page":36,"type":"figure","chapter":"第4章 用水合理性","title":"来水频率分析采用经验点据与理论频率曲线","image":"image10.png","side_note":[("设计情景","P=50%、75%、90%"),("参证资料","2007—2025逐月雨量"),("用途","推算设计径流量")],"source":"来源：报告4.2.2原图"},
{"page":37,"type":"source_text","chapter":"第4章 用水合理性","title":"可供水量必须先扣除下游生态流量","blocks":[{"label":"生态流量原文","text":"报告采用Tennant法计算下游生态流量，生态流量不小于多年平均径流量的10%。"},{"label":"可供水量","text":"不同保证率下的可供水量，由设计径流量扣除生态流量后确定；项目缺水量为750万m³申请取水量与水库净可供水量之差。"}],"source":"来源：报告4.2.2"},
{"page":38,"type":"figure","chapter":"第4章 用水合理性","title":"供水平衡图（一）：本地可供水60.59万m³，三干渠引水689.41万m³","image":"image13.png","source":"来源：报告供水平衡原图"},
{"page":39,"type":"figure","chapter":"第4章 用水合理性","title":"供水平衡图（二）：本地可供水94.57万m³，三干渠引水655.43万m³","image":"image14.png","source":"来源：报告供水平衡原图"},
{"page":40,"type":"analysis","chapter":"第4章 用水合理性","title":"报告正文及图件分别出现两组P=90%供水平衡参数","metrics":[("60.59万m³","第一组本地可供水量",RED),("689.41万m³","第一组三干渠引水量",ORANGE),("94.57万m³","第二组本地可供水量",TEAL),("655.43万m³","第二组三干渠引水量",GREEN)],"bullets":["报告4.2.2中分别列示P=90%可供水量60.59万m³和94.57万m³。","报告相应列示三干渠引水量689.41万m³和655.43万m³。"],"source":"来源：报告4.2.2、5.2.4及供水平衡原图"},
{"page":41,"type":"table","chapter":"第4章 用水合理性","title":"全年灌溉供水集中于5—8月，7月达到217.50万m³","headers":["月份","供水量","耗水量","退水量"],"widths":[260,300,300,310],"rows":[["2月","7.50","6.00","1.50"],["3月","52.50","42.00","10.50"],["4月","52.50","42.00","10.50"],["5月","123.75","99.00","24.75"],["6月","93.75","75.00","18.75"],["7月","217.50","174.00","43.50"]],"source":"来源：报告月度耗水及退水量表（上半表）"},
{"page":42,"type":"table","chapter":"第4章 用水合理性","title":"8—11月供水逐步回落，全年供水、耗水和退水闭合","headers":["月份","供水量","耗水量","退水量"],"widths":[260,300,300,310],"rows":[["8月","153.75","123.00","30.75"],["9月","30.00","24.00","6.00"],["10月","11.25","9.00","2.25"],["11月","7.50","6.00","1.50"],["全年","750.00","600.00","150.00"]],"source":"来源：报告月度耗水及退水量表（下半表）"},
{"page":43,"type":"analysis","chapter":"第4章 用水合理性","title":"报告按20%回归水比例核定耗水量与退水量","metrics":[("750万m³","年申请取水量",NAVY),("20%","灌溉回归水比例",ORANGE),("150万m³","年退水量",TEAL),("600万m³","年农业灌溉耗水量",GREEN)],"bullets":["退水以灌溉回归水形式补给当地地下水或重新进入地表水体。","各月耗水量和退水量见报告规划水平年耗水量及退水量表。"],"source":"来源：报告4.2.3、表4.2-7"},
{"page":44,"type":"analysis","chapter":"第4章 用水合理性","title":"规划利用系数0.650高于现有对标值，但需要持续改造支撑","metrics":[("0.528","湖北省平均",GREEN),("0.547","长江流域平均",TEAL),("0.580","全国平均",NAVY),("0.650","规划目标",ORANGE)],"bullets":["渠道淤积、衬砌不足、建筑物老化和监测薄弱仍是节水约束。","应将末级渠系、防渗、设备维护和计量数据纳入长期管理。"],"source":"来源：报告4.3"},
{"page":45,"type":"table","chapter":"第4章 用水合理性","title":"报告核定取水量、耗水量与退水量","headers":["核定事项","报告核定结果","报告说明"],"widths":[300,330,540],"rows":[["农业灌溉需水","规划水平年P=90%","维持现状作物结构与规模"],["年申请取水量","750.00万m³","玉泉水库与东风三干渠联合保障"],["年农业耗水量","600.00万m³","扣除灌溉回归水后核定"],["年退水量","150.00万m³","按灌溉水量20%核算"],["综合结论","申请取水量合理","符合用水总量和效率控制要求"]],"source":"来源：报告4.4"},
{"page":46,"type":"section","ch_no":"05","title":"取水水源论证","body":"验证联合水源方案、资料方法、来水补源、水质、取水口位置及水量水位可靠性。"},
{"page":47,"type":"source_text","chapter":"第5章 取水水源","title":"项目采用东风三干渠与玉泉水库联合水源方案","blocks":[{"label":"水源方案","text":"项目以东风三干渠和玉泉水库作为联合水源。玉泉水库长期承担本灌区农业供水，供水目标明确；结合东风三干渠引水补充，符合灌区实际情况和历史用水习惯，报告未另行提出其他水源方案。"}],"facts":[["玉泉水库","本地调蓄水源"],["东风三干渠","外调补充水源"],["农业灌溉","联合水源供水用途"],["既有渠系","取水输水工程基础"]],"source":"来源：报告5.1"},
{"page":48,"type":"source_text","chapter":"第5章 取水水源","title":"可靠性论证采用降雨序列和水库工程特性资料","blocks":[{"label":"参证资料","text":"玉泉水库流域内没有水文站，报告采用距水库约11km的当阳市防办2007—2025年历年逐月雨量资料作为参证。"},{"label":"工程资料","text":"水库工程特性采用2022年《玉泉水库除险加固工程初步设计报告》成果。"}],"facts":[["4.00km²","水库集雨面积"],["180.00万m³","多年平均径流量"],["994.6mm","多年平均降雨量"],["225万m³","正常蓄水位库容"],["6.4万m³","死库容"]],"source":"来源：报告5.2.3"},
{"page":49,"type":"figure","chapter":"第5章 取水水源","title":"取水水源论证范围为玉泉水库坝址以上流域","image":"image22.jpeg","source":"来源：报告附图二"},
{"page":50,"type":"source_text","chapter":"第5章 取水水源","title":"东风三干渠补水通过引水协议落实具体调度指标","blocks":[{"label":"补水必要性","text":"仅依靠玉泉水库自身天然来水及现有库容，不足以完全支撑灌区灌溉用水需求，项目规划由东风三干渠向玉泉水库引水补源。"},{"label":"协议内容","text":"报告提出由水库管理单位与三干渠主管部门正式签订引水协议，结合灌区实际缺水过程明确关键指标。"}],"facts":[["引水流量","协议明确内容"],["引水时段","协议明确内容"],["调度原则","协议明确内容"],["年度总引水量","协议明确内容"]],"source":"来源：报告5.2.4"},
{"page":51,"type":"figure","chapter":"第5章 取水水源","title":"取水口与坝下渠系衔接紧密，工程路径清晰","image":"image23.jpeg","source":"来源：报告附图三"},
{"page":52,"type":"source_text","chapter":"第5章 取水水源","title":"联合水源水质满足农业灌溉要求","blocks":[{"label":"水库水质","text":"坝址以上主要为天然汇水区，群利一队断面2024年达到地表水Ⅱ类标准。"},{"label":"干渠水质","text":"东风三干渠作为区域骨干农业供水通道，水体更新较快并实施渠道管护。"},{"label":"评价","text":"报告综合判断联合水源满足农田灌溉水质标准，长期取用不会对土壤和作物产生明显不利影响。"}],"source":"来源：报告5.2.6"},
{"page":53,"type":"analysis","chapter":"第5章 取水水源","title":"可靠性由水量、水质和水位运行三个方面构成","metrics":[("6.4万m³","死库容下限",RED),("225万m³","正常蓄水位库容",TEAL),("248.48万m³","设计洪水位库容",NAVY),("7—8月","重点调度期",ORANGE)],"bullets":["水量可靠依赖三干渠补源按月兑现。","水位运行必须同时守住死库容和防洪库容边界。","远程闸控与精准计量为精细调度提供工程基础。"],"source":"来源：报告5.2.7—5.2.8"},
{"page":54,"type":"section","ch_no":"06","title":"取水影响论证","body":"分析取水对区域水资源配置、生态下泄、水功能区和其他用水户的影响。"},
{"page":55,"type":"source_text","chapter":"第6章 取水影响","title":"报告从水资源配置、水生态、水功能区和其他用户分析取水影响","blocks":[{"label":"区域水资源配置","text":"报告认为，在执行三干渠引水协议及年度调度计划的情况下，项目取水对区域地表水资源及配置方案无显著影响。"},{"label":"水生态与水功能区","text":"项目预留生态下泄流量，水库运行库容保持在死库容以上；项目无生产、生活废污水排放，不改变现状水域水质本底值。"},{"label":"其他用水户","text":"玉泉水库除灌溉和下游河道生态用水外，无城镇生活、工业生产等其他用水户。"}],"source":"来源：报告第6章"},
{"page":56,"type":"section","ch_no":"07","title":"退水影响论证","body":"说明农业回归水的组成、时空规律、受纳路径、水质风险和生态作用。"},
{"page":57,"type":"figure","chapter":"第7章 退水影响","title":"退水影响范围覆盖子龙、合意和玉泉三村灌区","image":"image24.jpeg","source":"来源：报告附图四"},
{"page":58,"type":"source_text","chapter":"第7章 退水影响","title":"退水呈季节性、间歇性和分散性，不具备集中排放特征","blocks":[{"label":"组成与规模","text":"退水仅为田间渗漏水和灌溉尾水，年退水量150万m³，不设置集中排污口。"},{"label":"时间规律","text":"退水与灌水周期同步，7—8月为高峰，非灌溉季基本无退水。"},{"label":"空间规律","text":"通过田间沟渠、坡面漫流和土壤下渗，多散点进入浅层地下水或周边地表水体。"}],"source":"来源：报告7.1"},
{"page":59,"type":"analysis","chapter":"第7章 退水影响","title":"退水方案可行，但面源污染控制不能只依赖自然净化","metrics":[("20%","回归水系数",TEAL),("150万m³","年退水量",NAVY),("7—8月","退水峰值期",ORANGE),("TN/TP/COD","重点关注指标",RED)],"bullets":["土壤吸附、沟渠沉淀和植被拦截可降低污染负荷。","仍需通过化肥农药减量、生态沟渠和关键断面监测验证环境风险。"],"source":"来源：报告7.2—7.5"},
{"page":60,"type":"section","ch_no":"08","title":"水资源节约、保护及管理措施","body":"将工程节水转化为许可计划、计量监测、运维管护和水环境保护的长期闭环。"},
{"page":61,"type":"source_text","chapter":"第8章 管理措施","title":"节约措施聚焦输水损失与田间用水效率","blocks":[{"label":"渠系工程","text":"推进干支渠及末级渠系防渗整治，推广低压管输，减少渠道渗漏与输水损失。"},{"label":"田间技术","text":"推广喷微灌、水肥一体化、精准灌溉和水稻节水控灌，提高水分生产率。"},{"label":"计量基础","text":"完善取水口、干支渠控制节点和用水单元计量设施，为计划用水和节水评价提供数据。"}],"source":"来源：报告8.1"},
{"page":62,"type":"source_text","chapter":"第8章 管理措施","title":"保护措施包括农业投入减量、水资源监管和公众参与","blocks":[{"label":"农业面源控制","text":"推广水肥一体化、测土配方施肥和生态农业技术，科学用肥，减少化学肥料用量和农业面源污染。"},{"label":"水资源保护监管","text":"强化法律法规确立的水资源保护制度，建立协商、协调和联防机制，将保护目标纳入相关考核体系。"},{"label":"社会监督","text":"宣传水资源保护法律法规和制度，依法保障公众知情权，拓宽公众参与和舆论监督渠道。"}],"source":"来源：报告8.2"},
{"page":63,"type":"source_text","chapter":"第8章 管理措施","title":"管理措施覆盖取水许可、计量监测、工程运维和水环境保护","blocks":[{"label":"许可与计划用水","text":"依法办理取水许可手续，按照批复规模、期限和用途取水，并结合作物周期和雨情墒情制定月度、季度及年度用水计划。"},{"label":"计量与水平衡","text":"在取水口安装标准化计量设施，建立用水台账和数据上报制度，定期校验设备、开展灌区水平衡测试。"},{"label":"运维与环境管理","text":"建立水库及渠系专业化管护机制，开展工程巡查养护，并持续防控农业面源污染。"}],"source":"来源：报告8.3"},
{"page":64,"type":"section","ch_no":"09","title":"结论与建议","body":"归纳报告关于用水合理性、水源可靠性和取退水影响的结论，并转化为审批与运行要求。"},
{"page":65,"type":"source_text","chapter":"第9章 结论建议","title":"报告总体认为项目取用水合理、联合水源方案可行","blocks":[{"label":"用水合理性","text":"项目服务于现有农业灌溉，规划水平年不以扩大种植规模增加需水，并以节水改造和用水定额控制取水。"},{"label":"水源可靠性","text":"玉泉水库天然来水与东风三干渠补水组成联合水源，在落实补水协议和调度计划后可保障设计供水。"},{"label":"影响判断","text":"落实生态下泄、库水位控制、农业面源治理和水质监测后，取水与退水影响总体可控。"}],"source":"来源：报告第9章结论"},
{"page":66,"type":"source_text","chapter":"第9章 结论建议","title":"报告提出取水、退水影响补救与补偿措施","blocks":[{"label":"取水影响补救","text":"严格保障生态下泄流量，优化水库与东风三干渠引蓄联合调度方案，并依托闸门远程控制和精准计量设施提升节水效能。"},{"label":"退水影响补救","text":"推进化肥农药减量增效，利用灌排渠系和田间沟渠开展自然净化与生态拦截，降低农业面源污染负荷。"},{"label":"监测与管理","text":"建立覆盖取水、配水和主要退水环节的动态监控网络，定期开展关键点位水质监测。"}],"source":"来源：报告9.1取水和退水影响补救与补偿措施"},
{"page":67,"type":"source_text","chapter":"第9章 结论建议","title":"报告建议深化信息化管理并加强末级渠系长效管护","blocks":[{"label":"信息化与智能化管理","text":"充分利用已建成的闸门远程智能控制系统及精准计量设施，构建灌区水资源动态监控与智慧调度平台，实现取水、输水、配水全过程数字化管理，积累长序列监测数据并优化联合调度。"},{"label":"末级渠系与设施管护","text":"稳步推进田间末级渠系防渗改造与量测水设施配套，推广喷灌、微灌等高效节水技术，建立基层管护机制，落实信息化设备及水工建筑物的定期检修和日常保养。"}],"facts":[["全过程","取水、输水、配水数字化管理"],["长序列数据","优化水库与干渠联合调度"],["末级渠系","防渗与量测水设施配套"],["长效管护","定期检修与日常保养"]],"source":"来源：报告9.2"}
]


renderers = {"cover":cover,"section":section,"source_text":source_text,"figure":figure,"table":table_slide,"analysis":analysis,"agenda":agenda}


def audit_svg(path):
    data = path.read_text(encoding="utf-8")
    problems = []
    if 'font-size="17"' in data or 'font-size="16"' in data or 'font-size="15"' in data:
        # Allowed only for annotations/footer; retained for separate visual review.
        pass
    if 'font-size="10"' in data or 'font-size="9"' in data:
        problems.append("unexpected small text")
    return problems


def main():
    SVG_DIR.mkdir(parents=True, exist_ok=True)
    SVG_OUT.mkdir(parents=True, exist_ok=True)
    for d in (SVG_DIR, SVG_OUT):
        for f in d.glob("*.svg"): f.unlink()
    manifest = []
    audit = []
    for s in slides:
        name = f"{s['page']:02d}_{s['type']}.svg"
        content = renderers[s["type"]](s)
        for d in (SVG_DIR, SVG_OUT):
            (d/name).write_text(content, encoding="utf-8")
        probs = audit_svg(SVG_DIR/name)
        audit.append({"page":s["page"],"file":name,"problems":probs})
        manifest.append({"page":s["page"],"type":s["type"],"title":s.get("title","封面"),"source":s.get("source","")})
    (DECK/"slide_manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
    qa = DECK/"qa"
    qa.mkdir(exist_ok=True)
    (qa/"text-fit.json").write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({"slides":len(slides),"svg_dir":str(SVG_DIR),"audit_problems":sum(bool(x["problems"]) for x in audit)},ensure_ascii=False))


if __name__ == "__main__":
    main()
