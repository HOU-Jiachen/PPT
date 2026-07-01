You are a senior Chinese engineering-PPT reviewer. Review the following PPTX extraction. Return only JSON with keys passed:boolean, findings:[{severity,page,category,issue,fix}], and summary. Severity must be error or warning. Treat formatting, content faithfulness, layout, table readability, forbidden internal text, and chapter-emphasis misuse as review scope.

{
  "project": "东坡大道水土保持方案",
  "pptx": "C:\\Codex\\pptAgent\\ppt\\projects\\东坡大道水土保持方案\\exports\\东坡大道水土保持方案当前agent测试_44页_20260701_111514_review_round1_review_round2.pptx",
  "created_at": "2026-07-01T11:27:12",
  "slide_count": 44,
  "release_audit": {
    "errors": 0,
    "warnings": 2,
    "info": 1,
    "release_ready": true
  },
  "release_findings": [
    {
      "level": "warning",
      "code": "no-svg",
      "message": "No SVG output found; visual-content checks were skipped.",
      "context": {}
    },
    {
      "level": "warning",
      "code": "planned-table-rendered-without-native-table",
      "message": "Deck plan includes original table slides but no native PPTX table was available for structural comparison; verify source crops visually.",
      "context": {
        "planned_table_pages": [
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11,
          12,
          13,
          14,
          15,
          16,
          17,
          24,
          25,
          26,
          27,
          28,
          29,
          30,
          31,
          32,
          33,
          34,
          35
        ]
      }
    },
    {
      "level": "info",
      "code": "pptx-valid",
      "message": "PPTX package, XML, media, and parser checks passed.",
      "context": {
        "slides": 44
      }
    }
  ],
  "slides": [
    {
      "page": 1,
      "visible_text": "黄冈市东坡大道片区污水收集管网建设工程水土保持方案报告表汇报。 水土保持方案报告表 · 技术汇报。 围绕项目范围、防治责任、土石方平衡、水土流失预测、措施体系、投资概算和设施验收展开。 黄冈市住房和城市更新局。 01",
      "shape_count": 8,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "Rectangle 2",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "Rectangle 3",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.044,
            0.101,
            0.008,
            0.647
          ],
          "text": []
        },
        {
          "name": "title_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.065,
            0.115,
            0.81,
            0.18
          ],
          "text": [
            {
              "text": "黄冈市东坡大道片区污水收集管网建设工程水土保持方案报告表汇报。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "subtitle_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.068,
            0.333,
            0.638,
            0.047
          ],
          "text": [
            {
              "text": "水土保持方案报告表 · 技术汇报。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.068,
            0.424,
            0.735,
            0.109
          ],
          "text": [
            {
              "text": "围绕项目范围、防治责任、土石方平衡、水土流失预测、措施体系、投资概算和设施验收展开。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.068,
            0.776,
            0.6,
            0.037
          ],
          "text": [
            {
              "text": "黄冈市住房和城市更新局。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.876,
            0.909,
            0.048,
            0.027
          ],
          "text": [
            {
              "text": "01",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        }
      ]
    },
    {
      "page": 2,
      "visible_text": "汇报结构。 汇报结构沿报告七个技术章节展开。 02 结构按报告章节推进，先确认项目概况与防治责任，再核对评价、预测、措施、投资和验收管理。 01 综合说明与审批依据。 02 项目概况与工程布置。 03 防治责任范围与标准目标。 04 水土保持评价与土石方。 05 水土流失分析与预测。 06 水土保持措施与施工安排。 07 投资概算、效益与管理验收。",
      "shape_count": 27,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "汇报结构。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "汇报结构沿报告七个技术章节展开。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "02",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "body_text_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.054,
            0.163,
            0.855,
            0.059
          ],
          "text": [
            {
              "text": "结构按报告章节推进，先确认项目概况与防治责任，再核对评价、预测、措施、投资和验收管理。",
              "font_sizes": [],
              "emphasized_runs": 1
            }
          ]
        },
        {
          "name": "Rectangle 7",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.259,
            0.428,
            0.099
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.068,
            0.284,
            0.034,
            0.024
          ],
          "text": [
            {
              "text": "01",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.113,
            0.277,
            0.353,
            0.032
          ],
          "text": [
            {
              "text": "综合说明与审批依据。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 10",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.387,
            0.428,
            0.099
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.068,
            0.412,
            0.034,
            0.024
          ],
          "text": [
            {
              "text": "02",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.113,
            0.405,
            0.353,
            0.032
          ],
          "text": [
            {
              "text": "项目概况与工程布置。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 13",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.515,
            0.428,
            0.099
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.068,
            0.54,
            0.034,
            0.024
          ],
          "text": [
            {
              "text": "03",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.113,
            0.533,
            0.353,
            0.032
          ],
          "text": [
            {
              "text": "防治责任范围与标准目标。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 16",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.643,
            0.428,
            0.099
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.068,
            0.668,
            0.034,
            0.024
          ],
          "text": [
            {
              "text": "04",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.113,
            0.661,
            0.353,
            0.032
          ],
          "text": [
            {
              "text": "水土保持评价与土石方。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 19",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.504,
            0.259,
            0.428,
            0.099
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.518,
            0.284,
            0.034,
            0.024
          ],
          "text": [
            {
              "text": "05",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.563,
            0.277,
            0.353,
            0.032
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 22",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.504,
            0.387,
            0.428,
            0.099
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.518,
            0.412,
            0.034,
            0.024
          ],
          "text": [
            {
              "text": "06",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.563,
            0.405,
            0.353,
            0.032
          ],
          "text": [
            {
              "text": "水土保持措施与施工安排。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 25",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.504,
            0.515,
            0.428,
            0.099
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.518,
            0.54,
            0.034,
            0.024
          ],
          "text": [
            {
              "text": "07",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.563,
            0.533,
            0.353,
            0.032
          ],
          "text": [
            {
              "text": "投资概算、效益与管理验收。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        }
      ]
    },
    {
      "page": 3,
      "visible_text": "00 项目总览。 全局控制指标先行说明项目范围、预测结果、措施投资和验收闭环。 章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。 后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。 03",
      "shape_count": 8,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "Rectangle 2",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.115,
            0.012,
            0.643
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.133,
            0.075,
            0.043
          ],
          "text": [
            {
              "text": "00",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.213,
            0.66,
            0.083
          ],
          "text": [
            {
              "text": "项目总览。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.341,
            0.66,
            0.059
          ],
          "text": [
            {
              "text": "全局控制指标先行说明项目范围、预测结果、措施投资和验收闭环。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.445,
            0.705,
            0.077
          ],
          "text": [
            {
              "text": "章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.557,
            0.675,
            0.067
          ],
          "text": [
            {
              "text": "后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.909,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "03",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        }
      ]
    },
    {
      "page": 4,
      "visible_text": "项目总览。 项目范围、预测结果、措施投资和验收管理形成闭环。 04 1 项目范围：工程位于黄冈市黄州区城北片区，污水主管网6.2公里，预埋支管2.2公里。 2 预测结果：预测土壤流失总量104.05t，新增土壤流失量94.92t。 3 管理闭环：水土保持总投资26.9211万元，六项效益指标达到报告目标值。",
      "shape_count": 14,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "项目总览。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "项目范围、预测结果、措施投资和验收管理形成闭环。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "04",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.189,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.195,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.184,
            0.355,
            0.192
          ],
          "text": [
            {
              "text": "项目范围：工程位于黄冈市黄州区城北片区，污水主管网6.2公里，预埋支管2.2公里。",
              "font_sizes": [
                15.2,
                15.2,
                15.2,
                15.2,
                15.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.388,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.394,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.382,
            0.355,
            0.192
          ],
          "text": [
            {
              "text": "预测结果：预测土壤流失总量104.05t，新增土壤流失量94.92t。",
              "font_sizes": [
                15.2,
                15.2,
                15.2,
                15.2,
                15.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.586,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.592,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.58,
            0.355,
            0.192
          ],
          "text": [
            {
              "text": "管理闭环：水土保持总投资26.9211万元，六项效益指标达到报告目标值。",
              "font_sizes": [
                15.2,
                15.2,
                15.2,
                15.2,
                15.2
              ],
              "emphasized_runs": 5
            }
          ]
        }
      ]
    },
    {
      "page": 5,
      "visible_text": "01 综合说明与审批依据。 综合表和批复附件共同限定方案范围。 章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。 后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。 05",
      "shape_count": 8,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "Rectangle 2",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.115,
            0.012,
            0.643
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.133,
            0.075,
            0.043
          ],
          "text": [
            {
              "text": "01",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.213,
            0.66,
            0.083
          ],
          "text": [
            {
              "text": "综合说明与审批依据。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.341,
            0.66,
            0.059
          ],
          "text": [
            {
              "text": "综合表和批复附件共同限定方案范围。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.445,
            0.705,
            0.077
          ],
          "text": [
            {
              "text": "章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.557,
            0.675,
            0.067
          ],
          "text": [
            {
              "text": "后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.909,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "05",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        }
      ]
    },
    {
      "page": 6,
      "visible_text": "综合说明与审批依据。 综合报告表明确项目全局控制指标。 06 1 建设内容：东坡大道片区改造污水主管网6.2公里，沿线预埋支管2.2公里。 2 责任范围：防治责任范围为34416.00m²，均按管网工程区纳入。 3 投资口径：水土保持总投资26.9211万元，主体已列和方案新增分项计列。",
      "shape_count": 14,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "综合说明与审批依据。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "综合报告表明确项目全局控制指标。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "06",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.069,
            0.205,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.072,
            0.211,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.104,
            0.2,
            0.79,
            0.2
          ],
          "text": [
            {
              "text": "建设内容：东坡大道片区改造污水主管网6.2公里，沿线预埋支管2.2公里。",
              "font_sizes": [
                16.2,
                16.2,
                16.2,
                16.2,
                16.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.069,
            0.412,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.072,
            0.418,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.104,
            0.407,
            0.79,
            0.2
          ],
          "text": [
            {
              "text": "责任范围：防治责任范围为34416.00m²，均按管网工程区纳入。",
              "font_sizes": [
                16.2,
                16.2,
                16.2,
                16.2,
                16.2,
                16.2
              ],
              "emphasized_runs": 6
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.069,
            0.619,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.072,
            0.625,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.104,
            0.613,
            0.79,
            0.2
          ],
          "text": [
            {
              "text": "投资口径：水土保持总投资26.9211万元，主体已列和方案新增分项计列。",
              "font_sizes": [
                16.2,
                16.2,
                16.2
              ],
              "emphasized_runs": 3
            }
          ]
        }
      ]
    },
    {
      "page": 7,
      "visible_text": "02 项目概况与工程布置。 工程规模、占地、工期和施工组织决定扰动来源。 章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。 后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。 07",
      "shape_count": 8,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "Rectangle 2",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.115,
            0.012,
            0.643
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.133,
            0.075,
            0.043
          ],
          "text": [
            {
              "text": "02",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.213,
            0.66,
            0.083
          ],
          "text": [
            {
              "text": "项目概况与工程布置。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.341,
            0.66,
            0.059
          ],
          "text": [
            {
              "text": "工程规模、占地、工期和施工组织决定扰动来源。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.445,
            0.705,
            0.077
          ],
          "text": [
            {
              "text": "章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.557,
            0.675,
            0.067
          ],
          "text": [
            {
              "text": "后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.909,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "07",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        }
      ]
    },
    {
      "page": 8,
      "visible_text": "项目概况与工程布置。 工程特性表锁定规模、投资、工期和占地。 08 1 工程性质：项目为新建污水收集管网工程，建设地点为黄冈市黄州区。 2 投资工期：总投资8024.00万元，土建投资6914.95万元，建设期为13个月。 3 占地构成：总占地3.44hm²，报告按临时占地组织水土保持设计。",
      "shape_count": 14,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "项目概况与工程布置。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "工程特性表锁定规模、投资、工期和占地。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "08",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.069,
            0.205,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.072,
            0.211,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.104,
            0.2,
            0.79,
            0.2
          ],
          "text": [
            {
              "text": "工程性质：项目为新建污水收集管网工程，建设地点为黄冈市黄州区。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.069,
            0.412,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.072,
            0.418,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.104,
            0.407,
            0.79,
            0.2
          ],
          "text": [
            {
              "text": "投资工期：总投资8024.00万元，土建投资6914.95万元，建设期为13个月。",
              "font_sizes": [
                16.2,
                16.2,
                16.2,
                16.2,
                16.2,
                16.2,
                16.2
              ],
              "emphasized_runs": 7
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.069,
            0.619,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.072,
            0.625,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.104,
            0.613,
            0.79,
            0.2
          ],
          "text": [
            {
              "text": "占地构成：总占地3.44hm²，报告按临时占地组织水土保持设计。",
              "font_sizes": [
                16.2,
                16.2,
                16.2
              ],
              "emphasized_runs": 3
            }
          ]
        }
      ]
    },
    {
      "page": 9,
      "visible_text": "03 防治责任范围与标准目标。 责任范围和一级标准构成后续措施评价基准。 章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。 后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。 09",
      "shape_count": 8,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "Rectangle 2",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.115,
            0.012,
            0.643
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.133,
            0.075,
            0.043
          ],
          "text": [
            {
              "text": "03",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.213,
            0.66,
            0.083
          ],
          "text": [
            {
              "text": "防治责任范围与标准目标。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.341,
            0.66,
            0.059
          ],
          "text": [
            {
              "text": "责任范围和一级标准构成后续措施评价基准。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.445,
            0.705,
            0.077
          ],
          "text": [
            {
              "text": "章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.557,
            0.675,
            0.067
          ],
          "text": [
            {
              "text": "后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.909,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "09",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        }
      ]
    },
    {
      "page": 10,
      "visible_text": "防治责任范围与标准目标。 防治责任范围全部纳入管网工程区临时占地。 10 1 范围口径：管网工程区防治责任范围为34416.00m²。 2 用地类型：城镇村道路用地34151.00m²，公园与绿地265.00m²。 3 占地属性：报告表中永久占地为空，责任范围按临时占地纳入。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "防治责任范围与标准目标。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "防治责任范围全部纳入管网工程区临时占地。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "10",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "范围口径：管网工程区防治责任范围为34416.00m²。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "用地类型：城镇村道路用地34151.00m²，公园与绿地265.00m²。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "占地属性：报告表中永久占地为空，责任范围按临时占地纳入。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T006",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.48,
            0.881,
            0.276
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 11,
      "visible_text": "防治责任范围与标准目标。 防治责任范围全部纳入管网工程区临时占地（二） 11 1 用地类型：城镇村道路用地34151.00m²，公园与绿地265.00m²。 2 占地属性：报告表中永久占地为空，责任范围按临时占地纳入。 3 表内分项：城镇村道路用地。、公园与绿地。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "防治责任范围与标准目标。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "防治责任范围全部纳入管网工程区临时占地（二）",
              "font_sizes": [
                23.0,
                23.0
              ],
              "emphasized_runs": 2
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "11",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "用地类型：城镇村道路用地34151.00m²，公园与绿地265.00m²。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "占地属性：报告表中永久占地为空，责任范围按临时占地纳入。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "表内分项：城镇村道路用地。、公园与绿地。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "TableImage:T013",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.479,
            0.881,
            0.276
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 12,
      "visible_text": "防治责任范围与标准目标。 六项防治指标采用南方红壤区一级标准。 12 1 标准等级：项目执行南方红壤区建设类项目一级防治标准。 2 治理目标：水土流失治理度设计水平年目标为98% 3 控制目标：土壤流失控制比修正后设计水平年目标为1.0",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "防治责任范围与标准目标。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "六项防治指标采用南方红壤区一级标准。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "12",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "标准等级：项目执行南方红壤区建设类项目一级防治标准。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "治理目标：水土流失治理度设计水平年目标为98%",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 8
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "控制目标：土壤流失控制比修正后设计水平年目标为1.0",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 6
            }
          ]
        },
        {
          "name": "TableImage:T007",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.37,
            0.881,
            0.495
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 13,
      "visible_text": "项目概况与工程布置。 表土剥离量按公园与绿地扰动面积计列。 13 1 剥离对象：表土剥离面积为265.00m²，对应公园与绿地扰动区域。 2 剥离参数：表土层厚度0.3m，剥离厚度0.3m。 3 利用途径：表土剥离量79.5m³，后续用于管网工程区绿化覆土。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "项目概况与工程布置。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "表土剥离量按公园与绿地扰动面积计列。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "13",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "剥离对象：表土剥离面积为265.00m²，对应公园与绿地扰动区域。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "剥离参数：表土层厚度0.3m，剥离厚度0.3m。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "利用途径：表土剥离量79.5m³，后续用于管网工程区绿化覆土。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "TableImage:T014",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.545,
            0.881,
            0.146
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 14,
      "visible_text": "04 水土保持评价与土石方。 合规评价、土石方平衡和主体措施共同校核方案基础。 章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。 后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。 14",
      "shape_count": 8,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "Rectangle 2",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.115,
            0.012,
            0.643
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.133,
            0.075,
            0.043
          ],
          "text": [
            {
              "text": "04",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.213,
            0.66,
            0.083
          ],
          "text": [
            {
              "text": "水土保持评价与土石方。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.341,
            0.66,
            0.059
          ],
          "text": [
            {
              "text": "合规评价、土石方平衡和主体措施共同校核方案基础。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.445,
            0.705,
            0.077
          ],
          "text": [
            {
              "text": "章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.557,
            0.675,
            0.067
          ],
          "text": [
            {
              "text": "后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.909,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "14",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        }
      ]
    },
    {
      "page": 15,
      "visible_text": "水土保持评价与土石方。 土石方平衡显示弃方委托消纳、借方外购。 15 1 平衡关系：土石方开挖、回填、借方和弃方按工程分区分项列示。 2 弃方去向：弃方采用委托消纳方式处理。 3 借方来源：借方采用外购方式解决，报告未另列取土场。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土保持评价与土石方。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "土石方平衡显示弃方委托消纳、借方外购。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "15",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "平衡关系：土石方开挖、回填、借方和弃方按工程分区分项列示。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "弃方去向：弃方采用委托消纳方式处理。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "借方来源：借方采用外购方式解决，报告未另列取土场。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "TableImage:T015",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.422,
            0.881,
            0.39
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 16,
      "visible_text": "水土保持评价与土石方。 法律和技术标准评价结论均为符合。 16 1 法律条款：水土保持法相关制约性因素逐条评价为符合。 2 技术标准：报告按生产建设项目水土保持技术标准进行符合性分析。 3 长江保护：项目建设与长江保护法相关要求形成一致评价结论。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土保持评价与土石方。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "法律和技术标准评价结论均为符合。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "16",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "法律条款：水土保持法相关制约性因素逐条评价为符合。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "技术标准：报告按生产建设项目水土保持技术标准进行符合性分析。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "长江保护：项目建设与长江保护法相关要求形成一致评价结论。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T018",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.208,
            0.323,
            0.573,
            0.589
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 17,
      "visible_text": "水土保持评价与土石方。 法律和技术标准评价结论均为符合（三） 17 1 长江保护：项目建设与长江保护法相关要求形成一致评价结论。 2 表内分项：第四十九条。 3 表内分项：第六十一条。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土保持评价与土石方。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "法律和技术标准评价结论均为符合（三）",
              "font_sizes": [
                23.0,
                23.0,
                23.0
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "17",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "长江保护：项目建设与长江保护法相关要求形成一致评价结论。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "表内分项：第四十九条。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "表内分项：第六十一条。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "TableImage:T020",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.45,
            0.881,
            0.336
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 18,
      "visible_text": "水土保持评价与土石方。 主体工程已列措施以土地整治和铺种草皮为主。 18 1 工程措施：主体工程已列土地整治，数量按管网工程区计列。 2 植物措施：铺种草皮纳入主体工程已列投资。 3 投资关系：主体已列措施与方案新增措施共同构成防治体系。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土保持评价与土石方。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "主体工程已列措施以土地整治和铺种草皮为主。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "18",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "工程措施：主体工程已列土地整治，数量按管网工程区计列。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "植物措施：铺种草皮纳入主体工程已列投资。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "投资关系：主体已列措施与方案新增措施共同构成防治体系。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "TableImage:T021",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.424,
            0.881,
            0.387
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 19,
      "visible_text": "05 水土流失分析与预测。 预测范围、侵蚀模数和流失量形成防护强度依据。 章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。 后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。 19",
      "shape_count": 8,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "Rectangle 2",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.115,
            0.012,
            0.643
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.133,
            0.075,
            0.043
          ],
          "text": [
            {
              "text": "05",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.213,
            0.66,
            0.083
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.341,
            0.66,
            0.059
          ],
          "text": [
            {
              "text": "预测范围、侵蚀模数和流失量形成防护强度依据。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.445,
            0.705,
            0.077
          ],
          "text": [
            {
              "text": "章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.557,
            0.675,
            0.067
          ],
          "text": [
            {
              "text": "后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.909,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "19",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        }
      ]
    },
    {
      "page": 20,
      "visible_text": "水土流失分析与预测。 预测范围与防治责任范围保持一致。 20 1 预测单元：预测范围为管网工程区，面积与防治责任范围一致。 2 扰动面积：扰动地表面积按34416.00m²纳入预测。 3 时段划分：施工期和自然恢复期分别列示预测参数。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "预测范围与防治责任范围保持一致。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "20",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "预测单元：预测范围为管网工程区，面积与防治责任范围一致。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "扰动面积：扰动地表面积按34416.00m²纳入预测。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "时段划分：施工期和自然恢复期分别列示预测参数。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "TableImage:T023",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.479,
            0.881,
            0.276
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 21,
      "visible_text": "水土流失分析与预测。 预测范围与防治责任范围保持一致（二） 21 1 扰动面积：扰动地表面积按34416.00m²纳入预测。 2 时段划分：施工期和自然恢复期分别列示预测参数。 3 表内分项：公园与绿地。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "预测范围与防治责任范围保持一致（二）",
              "font_sizes": [
                23.0,
                23.0,
                23.0
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "21",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "扰动面积：扰动地表面积按34416.00m²纳入预测。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "时段划分：施工期和自然恢复期分别列示预测参数。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "表内分项：公园与绿地。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "TableImage:T024",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.475,
            0.881,
            0.285
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 22,
      "visible_text": "水土流失分析与预测。 预测范围与防治责任范围保持一致（三） 22 1 时段划分：施工期和自然恢复期分别列示预测参数。 2 表内分项：植被破坏型一般扰动地表。、265.00",
      "shape_count": 12,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "预测范围与防治责任范围保持一致（三）",
              "font_sizes": [
                23.0,
                23.0,
                23.0
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "22",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.063
          ],
          "text": [
            {
              "text": "时段划分：施工期和自然恢复期分别列示预测参数。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.249,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.255,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.243,
            0.842,
            0.063
          ],
          "text": [
            {
              "text": "表内分项：植被破坏型一般扰动地表。、265.00",
              "font_sizes": [
                14.2,
                14.2
              ],
              "emphasized_runs": 2
            }
          ]
        },
        {
          "name": "TableImage:T025",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.499,
            0.881,
            0.237
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 23,
      "visible_text": "水土流失分析与预测。 预测范围与防治责任范围保持一致（四） 23 1 预测单元：预测范围为管网工程区，面积与防治责任范围一致。 2 扰动面积：扰动地表面积按34416.00m²纳入预测。",
      "shape_count": 12,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "预测范围与防治责任范围保持一致（四）",
              "font_sizes": [
                23.0,
                23.0,
                23.0
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "23",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.063
          ],
          "text": [
            {
              "text": "预测单元：预测范围为管网工程区，面积与防治责任范围一致。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.249,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.255,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.243,
            0.842,
            0.063
          ],
          "text": [
            {
              "text": "扰动面积：扰动地表面积按34416.00m²纳入预测。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T026",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.524,
            0.881,
            0.186
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 24,
      "visible_text": "水土流失分析与预测。 背景土壤侵蚀模数由占地类型加权形成。 24 1 类型参数：城镇村道路用地平均土壤侵蚀模数为260t/(km²·a)。 2 绿地参数：公园与绿地平均土壤侵蚀模数为450t/(km²·a)。 3 加权结果：报告列示背景土壤侵蚀模数为261.46t/(km²·a)。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "背景土壤侵蚀模数由占地类型加权形成。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "24",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "类型参数：城镇村道路用地平均土壤侵蚀模数为260t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "绿地参数：公园与绿地平均土壤侵蚀模数为450t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "加权结果：报告列示背景土壤侵蚀模数为261.46t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T027",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.518,
            0.881,
            0.198
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 25,
      "visible_text": "水土流失分析与预测。 背景土壤侵蚀模数由占地类型加权形成（二） 25 1 绿地参数：公园与绿地平均土壤侵蚀模数为450t/(km²·a)。 2 加权结果：报告列示背景土壤侵蚀模数为261.46t/(km²·a)。 3 表内分项：城镇村道路用地。、公园与绿地。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "背景土壤侵蚀模数由占地类型加权形成（二）",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "25",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "绿地参数：公园与绿地平均土壤侵蚀模数为450t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "加权结果：报告列示背景土壤侵蚀模数为261.46t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "表内分项：城镇村道路用地。、公园与绿地。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "TableImage:T028",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.48,
            0.881,
            0.275
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 26,
      "visible_text": "水土流失分析与预测。 施工期侵蚀模数显著高于背景值。 26 1 植被破坏型：施工期土壤侵蚀模数为1153.34t/(km²·a)。 2 地表翻扰型：施工期土壤侵蚀模数为3032.58t/(km²·a)。 3 综合取值：施工期综合取值为3018.60t/(km²·a)。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "施工期侵蚀模数显著高于背景值。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "26",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "植被破坏型：施工期土壤侵蚀模数为1153.34t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "地表翻扰型：施工期土壤侵蚀模数为3032.58t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "综合取值：施工期综合取值为3018.60t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T030",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.168,
            0.323,
            0.652,
            0.589
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 27,
      "visible_text": "水土流失分析与预测。 施工期侵蚀模数显著高于背景值（二） 27 1 地表翻扰型：施工期土壤侵蚀模数为3032.58t/(km²·a)。 2 综合取值：施工期综合取值为3018.60t/(km²·a)。 3 表内分项：1.1、降雨侵蚀力因子。、R。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "施工期侵蚀模数显著高于背景值（二）",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "27",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "地表翻扰型：施工期土壤侵蚀模数为3032.58t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "综合取值：施工期综合取值为3018.60t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "表内分项：1.1、降雨侵蚀力因子。、R。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T031",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.21,
            0.323,
            0.568,
            0.589
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 28,
      "visible_text": "水土流失分析与预测。 施工期侵蚀模数显著高于背景值（三） 28 1 综合取值：施工期综合取值为3018.60t/(km²·a)。 2 表内分项：1.2、土壤可蚀性因子。、K。 3 表内分项：1.3、坡长因子。、Ly。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "施工期侵蚀模数显著高于背景值（三）",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "28",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "综合取值：施工期综合取值为3018.60t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "表内分项：1.2、土壤可蚀性因子。、K。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "表内分项：1.3、坡长因子。、Ly。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T032",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.114,
            0.323,
            0.761,
            0.589
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 29,
      "visible_text": "水土流失分析与预测。 施工期侵蚀模数显著高于背景值（四） 29 1 植被破坏型：施工期土壤侵蚀模数为1153.34t/(km²·a)。 2 地表翻扰型：施工期土壤侵蚀模数为3032.58t/(km²·a)。",
      "shape_count": 12,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "施工期侵蚀模数显著高于背景值（四）",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "29",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.063
          ],
          "text": [
            {
              "text": "植被破坏型：施工期土壤侵蚀模数为1153.34t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.249,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.255,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.243,
            0.842,
            0.063
          ],
          "text": [
            {
              "text": "地表翻扰型：施工期土壤侵蚀模数为3032.58t/(km²·a)。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T033",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.523,
            0.881,
            0.189
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 30,
      "visible_text": "水土流失分析与预测。 预测土壤流失总量104.05t，新增量94.92t。 30 1 预测总量：项目预测土壤流失总量为104.05t。 2 新增量：新增土壤流失量为94.92t。 3 重点时段：施工期是新增水土流失控制重点。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土流失分析与预测。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "预测土壤流失总量104.05t，新增量94.92t。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "30",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "预测总量：项目预测土壤流失总量为104.05t。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "新增量：新增土壤流失量为94.92t。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "重点时段：施工期是新增水土流失控制重点。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T034",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.521,
            0.881,
            0.192
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 31,
      "visible_text": "06 水土保持措施与施工安排。 分区措施、工程量和施工窗口形成实施路径。 章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。 后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。 31",
      "shape_count": 8,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "Rectangle 2",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.115,
            0.012,
            0.643
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.133,
            0.075,
            0.043
          ],
          "text": [
            {
              "text": "06",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.213,
            0.66,
            0.083
          ],
          "text": [
            {
              "text": "水土保持措施与施工安排。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.341,
            0.66,
            0.059
          ],
          "text": [
            {
              "text": "分区措施、工程量和施工窗口形成实施路径。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.445,
            0.705,
            0.077
          ],
          "text": [
            {
              "text": "章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.557,
            0.675,
            0.067
          ],
          "text": [
            {
              "text": "后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.909,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "31",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        }
      ]
    },
    {
      "page": 32,
      "visible_text": "水土保持措施与施工安排。 防治分区为管网工程区，防治面积34416.00m²。 32 1 分区设置：报告将项目区划分为管网工程区。 2 防治面积：管网工程区防治面积为34416.00m²。 3 管理对象：永久占地为空，临时占地承担主要防治任务。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土保持措施与施工安排。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "防治分区为管网工程区，防治面积34416.00m²。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "32",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "分区设置：报告将项目区划分为管网工程区。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "防治面积：管网工程区防治面积为34416.00m²。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "管理对象：永久占地为空，临时占地承担主要防治任务。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "TableImage:T035",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.502,
            0.881,
            0.231
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 33,
      "visible_text": "水土保持措施与施工安排。 措施体系覆盖工程、植物和临时三类措施。 33 1 工程措施：主体已有土地整治，方案新增表土剥离和表土回覆。 2 植物措施：主体已有铺种草皮。 3 临时措施：报告列示临时苫盖、高压洗车池和临时排水沉沙措施。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土保持措施与施工安排。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "措施体系覆盖工程、植物和临时三类措施。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "33",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "工程措施：主体已有土地整治，方案新增表土剥离和表土回覆。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "植物措施：主体已有铺种草皮。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "临时措施：报告列示临时苫盖、高压洗车池和临时排水沉沙措施。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "TableImage:T036",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.49,
            0.881,
            0.255
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 34,
      "visible_text": "水土保持措施与施工安排。 措施体系覆盖工程、植物和临时三类措施（二） 34 1 植物措施：主体已有铺种草皮。 2 临时措施：报告列示临时苫盖、高压洗车池和临时排水沉沙措施。 3 表内分项：表土回覆。、m³。、79.5",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土保持措施与施工安排。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "措施体系覆盖工程、植物和临时三类措施（二）",
              "font_sizes": [
                23.0,
                23.0,
                23.0,
                23.0
              ],
              "emphasized_runs": 4
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "34",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "植物措施：主体已有铺种草皮。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "临时措施：报告列示临时苫盖、高压洗车池和临时排水沉沙措施。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 5
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "表内分项：表土回覆。、m³。、79.5",
              "font_sizes": [
                14.2,
                14.2
              ],
              "emphasized_runs": 2
            }
          ]
        },
        {
          "name": "TableImage:T037",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.427,
            0.881,
            0.381
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 35,
      "visible_text": "水土保持措施与施工安排。 措施实施进度嵌入2025—2026年施工窗口。 35 1 工期窗口：水土保持工程施工衔接2025年12月至2026年12月。 2 措施节奏：临时防护、表土措施和植物措施按施工过程分期安排。 3 进度关系：措施实施与主体工程施工时序保持同步。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "水土保持措施与施工安排。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "措施实施进度嵌入2025—2026年施工窗口。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "35",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "工期窗口：水土保持工程施工衔接2025年12月至2026年12月。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 7
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "措施节奏：临时防护、表土措施和植物措施按施工过程分期安排。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 8
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "进度关系：措施实施与主体工程施工时序保持同步。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T038",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.396,
            0.881,
            0.443
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 36,
      "visible_text": "07 投资概算、效益与管理验收。 投资、补偿费、效益和验收管理形成闭环。 章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。 后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。 36",
      "shape_count": 8,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "Rectangle 2",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.115,
            0.012,
            0.643
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.133,
            0.075,
            0.043
          ],
          "text": [
            {
              "text": "07",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.213,
            0.66,
            0.083
          ],
          "text": [
            {
              "text": "投资概算、效益与管理验收。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.341,
            0.66,
            0.059
          ],
          "text": [
            {
              "text": "投资、补偿费、效益和验收管理形成闭环。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.445,
            0.705,
            0.077
          ],
          "text": [
            {
              "text": "章节内容保留报告中的源表、控制值和工程关系，并把范围、目标、措施、投资。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "body_text_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.078,
            0.557,
            0.675,
            0.067
          ],
          "text": [
            {
              "text": "后续页面以该章节证据为核心，展示原始表格、计算参数或报告结论。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.909,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "36",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        }
      ]
    },
    {
      "page": 37,
      "visible_text": "投资概算、效益与管理验收。 水土保持总投资26.9211万元。 37 1 总投资：水土保持总投资为26.9211万元。 2 分项构成：新增投资、主体工程已列投资和独立费用分项计列。 3 费用关系：工程措施、植物措施和临时措施共同进入概算体系。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "投资概算、效益与管理验收。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "水土保持总投资26.9211万元。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "37",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.195,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.201,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.189,
            0.299,
            0.227
          ],
          "text": [
            {
              "text": "总投资：水土保持总投资为26.9211万元。",
              "font_sizes": [
                14.5,
                14.5,
                14.5
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.428,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.434,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.423,
            0.299,
            0.227
          ],
          "text": [
            {
              "text": "分项构成：新增投资、主体工程已列投资和独立费用分项计列。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.661,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.667,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.656,
            0.299,
            0.227
          ],
          "text": [
            {
              "text": "费用关系：工程措施、植物措施和临时措施共同进入概算体系。",
              "font_sizes": [
                14.5,
                14.5,
                14.5,
                14.5,
                14.5,
                14.5,
                14.5
              ],
              "emphasized_runs": 7
            }
          ]
        },
        {
          "name": "TableImage:T040",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.407,
            0.236,
            0.519,
            0.622
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 38,
      "visible_text": "投资概算、效益与管理验收。 水土保持总投资26.9211万元（二） 38 1 分项构成：新增投资、主体工程已列投资和独立费用分项计列。 2 费用关系：工程措施、植物措施和临时措施共同进入概算体系。 3 表内分项：（一）、管网工程区。、0.1827",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "投资概算、效益与管理验收。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "水土保持总投资26.9211万元（二）",
              "font_sizes": [
                23.0,
                23.0,
                23.0
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "38",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "分项构成：新增投资、主体工程已列投资和独立费用分项计列。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "费用关系：工程措施、植物措施和临时措施共同进入概算体系。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 7
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "表内分项：（一）、管网工程区。、0.1827",
              "font_sizes": [
                14.2,
                14.2
              ],
              "emphasized_runs": 2
            }
          ]
        },
        {
          "name": "TableImage:T041",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.439,
            0.881,
            0.356
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 39,
      "visible_text": "投资概算、效益与管理验收。 水土保持总投资26.9211万元（三） 39 1 费用关系：工程措施、植物措施和临时措施共同进入概算体系。 2 表内分项：1、铺种草皮。、m²。",
      "shape_count": 12,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "投资概算、效益与管理验收。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "水土保持总投资26.9211万元（三）",
              "font_sizes": [
                23.0,
                23.0,
                23.0
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "39",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.063
          ],
          "text": [
            {
              "text": "费用关系：工程措施、植物措施和临时措施共同进入概算体系。",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 7
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.249,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.255,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.243,
            0.842,
            0.063
          ],
          "text": [
            {
              "text": "表内分项：1、铺种草皮。、m²。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T042",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.491,
            0.881,
            0.252
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 40,
      "visible_text": "投资概算、效益与管理验收。 水土保持总投资26.9211万元（四） 40 1 总投资：水土保持总投资为26.9211万元。 2 分项构成：新增投资、主体工程已列投资和独立费用分项计列。 3 表内分项：2、高压洗车机。、台。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "投资概算、效益与管理验收。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "水土保持总投资26.9211万元（四）",
              "font_sizes": [
                23.0,
                23.0,
                23.0
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "40",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "总投资：水土保持总投资为26.9211万元。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "分项构成：新增投资、主体工程已列投资和独立费用分项计列。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "表内分项：2、高压洗车机。、台。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T043",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.442,
            0.881,
            0.35
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 41,
      "visible_text": "投资概算、效益与管理验收。 水土保持总投资26.9211万元（五） 41 1 总投资：水土保持总投资为26.9211万元。 2 分项构成：新增投资、主体工程已列投资和独立费用分项计列。 3 表内分项：（五）、水土保持设施验收报告编制。、10.3100",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "投资概算、效益与管理验收。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "水土保持总投资26.9211万元（五）",
              "font_sizes": [
                23.0,
                23.0,
                23.0
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "41",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "总投资：水土保持总投资为26.9211万元。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "分项构成：新增投资、主体工程已列投资和独立费用分项计列。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "表内分项：（五）、水土保持设施验收报告编制。、10.3100",
              "font_sizes": [
                14.2,
                14.2
              ],
              "emphasized_runs": 2
            }
          ]
        },
        {
          "name": "TableImage:T044",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.436,
            0.881,
            0.363
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 42,
      "visible_text": "投资概算、效益与管理验收。 水土保持补偿费51624元符合免征情形。 42 1 征占面积：补偿费计算面积为34416m²。 2 计费标准：报告列示收费标准为1.5元/m²。 3 计算金额：水土保持补偿费为51624元，并列明免征依据。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "投资概算、效益与管理验收。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "水土保持补偿费51624元符合免征情形。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "42",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "征占面积：补偿费计算面积为34416m²。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "计费标准：报告列示收费标准为1.5元/m²。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "计算金额：水土保持补偿费为51624元，并列明免征依据。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T045",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.054,
            0.525,
            0.881,
            0.185
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 43,
      "visible_text": "投资概算、效益与管理验收。 六项防治效益指标达到报告目标值。 43 1 治理度：水土流失总治理度设计达到值为99.99% 2 控制比：土壤流失控制比设计达到值满足报告目标。 3 效益结论：各项防治效益评估结果均为达标。",
      "shape_count": 15,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "投资概算、效益与管理验收。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "六项防治效益指标达到报告目标值。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "43",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.179,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.185,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.173,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "治理度：水土流失总治理度设计达到值为99.99%",
              "font_sizes": [
                14.2,
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 4
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.225,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.231,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.22,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "控制比：土壤流失控制比设计达到值满足报告目标。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.054,
            0.272,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.057,
            0.278,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.089,
            0.267,
            0.842,
            0.056
          ],
          "text": [
            {
              "text": "效益结论：各项防治效益评估结果均为达标。",
              "font_sizes": [
                14.2,
                14.2,
                14.2
              ],
              "emphasized_runs": 3
            }
          ]
        },
        {
          "name": "TableImage:T048",
          "type": "PICTURE (13)",
          "bbox_ratio": [
            0.072,
            0.323,
            0.844,
            0.589
          ],
          "picture": true
        }
      ]
    },
    {
      "page": 44,
      "visible_text": "投资概算、效益与管理验收。 验收管理落实后形成水土保持闭环。 44 1 监理管理：水土保持监理纳入工程建设管理过程。 2 设施验收：水土保持设施验收完成后，工程闭环进入运行阶段。 3 资料管理：报告成果、验收资料和公开要求共同支撑后续管理。 水土保持设施验收完成后，项目形成措施、投资、效益和资料管理闭环。",
      "shape_count": 16,
      "shapes": [
        {
          "name": "Rectangle 1",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.0,
            0.0,
            1.0,
            1.0
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.029,
            0.66,
            0.032
          ],
          "text": [
            {
              "text": "投资概算、效益与管理验收。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "title_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.035,
            0.075,
            0.855,
            0.067
          ],
          "text": [
            {
              "text": "验收管理落实后形成水土保持闭环。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.889,
            0.045,
            0.041,
            0.027
          ],
          "text": [
            {
              "text": "44",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 5",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.035,
            0.149,
            0.893,
            0.003
          ],
          "text": []
        },
        {
          "name": "Rectangle 6",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.074,
            0.216,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.222,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "1",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.109,
            0.211,
            0.557,
            0.138
          ],
          "text": [
            {
              "text": "监理管理：水土保持监理纳入工程建设管理过程。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 9",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.074,
            0.36,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.366,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "2",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.109,
            0.355,
            0.557,
            0.138
          ],
          "text": [
            {
              "text": "设施验收：水土保持设施验收完成后，工程闭环进入运行阶段。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 12",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.074,
            0.505,
            0.026,
            0.04
          ],
          "text": []
        },
        {
          "name": "page_meta_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.077,
            0.511,
            0.019,
            0.019
          ],
          "text": [
            {
              "text": "3",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "bullet_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.109,
            0.5,
            0.557,
            0.138
          ],
          "text": [
            {
              "text": "资料管理：报告成果、验收资料和公开要求共同支撑后续管理。",
              "font_sizes": [],
              "emphasized_runs": 0
            }
          ]
        },
        {
          "name": "Rectangle 15",
          "type": "AUTO_SHAPE (1)",
          "bbox_ratio": [
            0.074,
            0.701,
            0.788,
            0.083
          ],
          "text": []
        },
        {
          "name": "body_text_emphasis_textbox",
          "type": "TEXT_BOX (17)",
          "bbox_ratio": [
            0.092,
            0.724,
            0.735,
            0.027
          ],
          "text": [
            {
              "text": "水土保持设施验收完成后，项目形成措施、投资、效益和资料管理闭环。",
              "font_sizes": [
                16.0,
                16.0,
                16.0
              ],
              "emphasized_runs": 3
            }
          ]
        }
      ]
    }
  ],
  "review_rules": [
    "Visible content must be source-faithful Chinese engineering report language.",
    "Do not allow internal IDs such as T036, T-036, evidence IDs, filenames, source_mode, or generation-process wording.",
    "Do not allow generic process sentences such as key values remain checkable against source tables.",
    "Tables must be readable; native table text below 10 pt or source-table crops marked TableImageNeedsSplit are blocking.",
    "Chapter divider names and chapter-introduction text must not use colored emphasis; emphasis is limited to substantive body content.",
    "Flag overlap, cramped layout, excessive density, incomplete sentences, poor table formatting, and missing evidence context."
  ]
}