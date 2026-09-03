# 图像生成与交付

这是图像工具调用、输入顺序、提示词与交付行为的唯一真源。生成前检查见 [preflight-gates.md](preflight-gates.md)；成图后不自动评分、proof 或重试。

## 运行目录与依赖

```text
output/yingzao/<run-id>/
  inputs/                 # 校正副本，不改原文件
  analysis/               # preflight、事实卡、brief、glyph brief、typeset spec/report
  drafts/                 # 仅用户要求探索时使用
  final/                  # 海报和可选对照
  recipe-history.json
```

先运行 `python3 scripts/check_dependencies.py`。所有依赖型脚本通过 `_runtime.py` 在调用者目录及父目录寻找兼容 `.venv`；也可由 `CAP_PYTHON` 指定隔离解释器。自动发现失败时停止并报告，不能全局安装或把缺包当成通过。只有用户授权后，才在调用者工作目录的隔离环境执行 `python -m pip install -r <skill>/requirements.txt`。

脚本不得把缓存、目录 HTML、测试图或运行产物写回 Skill 包。

## 动作与固定输入顺序

单图与同址多图融合默认用 edit：

```text
Image 1 — EDIT TARGET：真实几何与身份的唯一来源
Image 2 — PRIMARY VISUAL REFERENCE：整体迁移构图机制、主体处理、材质层级和图文张力；不复制其建筑、文字或符号
Image 3 — TYPESET GUIDE：只使用已确认文案、真实字面、共同轴、阅读顺序和实际主体轮廓遮挡；不含目标照片像素或最终风格
Image 4+ — 可选同址主体来源：只使用逐张点名的对象
```

主导参考必须是真实图像输入，优先用 `recipe <id> --json` 返回的 `quality=plate` 资产；无 plate 才用 thumbnail。多图逐张说明可用内容、身份锚点和禁止迁移内容。

文字路径：

- `typeset-guide-integrated`：默认正式路径；垫图与原图、参考同次送入 edit。
- `model-native-minimal-text`：门控不可用、文案极少或用户只要快速探索时使用。
- `geometry-only`：只约束主体范围、轴线与遮挡方向；仍保留 Image 2。
- `layered-final-type`：仅用户在生成前明确要求逐字绝对准确并接受程序字层时使用，不能因模型写字失败自动切换。

## GPT-Image-2 参数

直接调用 Images API 时：`model=gpt-image-2`；真实照片走 `/v1/images/edits`；正式成图用 `quality=high`，只有用户明确要求快速探索才用 `low/medium`；省略 `input_fidelity`；省略 `background` 或使用不透明背景，不能请求 `transparent`。多图作为独立 `image[]`，第一张始终是 edit target，蒙版只作用于第一张。

| 比例 | 尺寸 |
| --- | --- |
| 3:4 | `1536x2048` |
| 4:3 | `2048x1536` |
| 16:9 | `2048x1152` |
| 9:16 | `1152x2048` |
| 1:1 | `1536x1536` |

边长不超过 3840px、两边为 16 的倍数、长短边不超过 3:1、总像素 655,360–8,294,400。工具不暴露尺寸时先声明方向与安全区，生成后用 `fit_canvas.py` 做确定性 crop 或 pad，不拉伸；身份锚点余量不足时用 pad。

## 模型要完成的工作

优先级：`真实身份 > 参考无关的四域命题 > 主导参考的完整机制 > 垫图空间关系 > 局部像素`。

- **主体域**：语义抠取，并发生尺度/位置重组或屋面、木构、墙体、器物、食物等分区材质转译。
- **背景域**：建立服务构图的色场、色窗、明度切片、负形或重建空间，不能只保留原天空或拉普通渐变。
- **互动域**：让真实檐口、屋脊、柱列、器物或食物轮廓与标题/色形产生遮挡、共边、穿插或负形咬合。
- **构图修复**：先识别原图的稳定骨架，只修一个主问题；允许补齐可连续推断的背景、直柱、墙、水面或地面，不发明屋顶、层数、门窗、雕塑或镜像构件。

普通裁切、统一滤镜、矩形拼版、网页式卡片或纯文字叠加不构成图像模型增值。主导参考提供的是整体设计逻辑，不是给成品加一层“参考色”。

## 前置排版与字形

```bash
python3 scripts/typeset_compose.py blank analysis/typeset-spec.json analysis/typeset-guide.png \
  --report analysis/typeset-report.json
```

报告必须通过字体 cmap、fallback、真实字面、碰撞、溢出、共享轴、primitive 禁穿区、遮挡契约与竖排顺序。垫图保持中性灰阶；不含最终配色、纹理、完整主体矩形或网页容器。

`reinterpret` 必须已有 `analysis/glyph-brief.md`。Image 3 只锁字面范围、共同轴与阅读顺序；模型按一个清楚形制重绘展示字。地点、年代、拼音和资料字保持 `literal`，并可使用不同常规字族建立层级。

## 最小提示词

只写本方案使用的内容：

```text
Action: edit the corrected target; do not invent a new place or building.
Image roles: <逐张角色与禁止迁移内容>
Composition diagnosis: <preserve 的理由，或一个主问题>
Composition repair: <一个主动作 + 可安全延续区域 + 可见结果 + 文字进入方式>
Creative thesis: <主体提取/尺度/材料 + 主动背景 + 真实轮廓互动 + 非默认排版动作>
Reference transfer: <Image 2 如何强化上述整体机制，以及占幅、负空间和互动边界的对应>
Identity invariants: <3–5 个决定身份的几何、题字或构件>
Typography behavior: <Image 3 的标题组、共同轴、换行、阅读顺序与遮挡；不复制其颜色和 primitive>
Display glyph design: <reinterpret 时写形制、逐字补偿和建筑对应；小字 literal>
Text (verbatim): <必要短文案>
Do not add: <不超过 5 个灾难性错误>
```

不要附 Token ID、门控条目或历史问题清单。原构图成立时写 `preserve`，保护偏心、框景、对角动势或横向跨越；不为模板强行居中、对称或补全。

## 交付与反馈

按预先确认数量生成并保存到 `final/`。用户要求原图对照时运行 `make_comparison.py`；否则直接交付海报。交付时邀请用户指出字体、主体、构图、材质、文案或融合关系中的具体问题。

收到反馈后才修订：

- 局部字形、错字、边缘、小范围材质：以当前成图为 edit target，只改反馈范围，锁定其他像素。
- 主体处理、背景色场、主布局、参考方向或图文关系：回到校正原图，重做四域命题、参考选择与垫图；不在失败拓扑上继续补丁。
- 只针对展示字时复用并更新 `glyph-brief.md`，仍由模型重绘，不自动后贴字。

修改后交回用户；下一轮是否继续由用户决定，没有隐藏重试。

首次交付一张新海报后，再问一次是否扩展为九宫格视频分镜与视频提示词。只有用户同意才读取 [video-storyboard.md](video-storyboard.md)，且不自动生成视频。
