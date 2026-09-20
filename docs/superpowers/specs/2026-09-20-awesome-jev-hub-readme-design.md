# Awesome Jev Hub README 设计

## 目标

第一阶段将 `awesome-jev-hub` 建成中英双语、证据优先的 Jev 开发者资源入口。首个交付只包含 README 目录和第一部分 `Run Jev Now / 立即体验`，暂不展开其余栏目。

## 受众

- 第一次接触 Jev、希望立即运行示例的开发者
- 希望把 Jev 接入 Codex、Claude Code 等 Agent 的实践者
- 需要比较项目可信度、复现情况和维护状态的技术决策者

## 内容原则

- 中文与英文内容保持相同结构，分别维护在 `README.md` 和 `README_EN.md`。
- 官方声明、作者自测和第三方复现必须明确区分。
- 动态信息标注核查日期；价格、限额、模型版本等不写成永久事实。
- 一个资源只进入一个主分类，其他属性使用标签表达。
- 每个项目至少说明：解决的问题、Jev 承担的决策、运行入口、验证状态和最后核查日期。

## README 目录

1. Run Jev Now / 立即体验
2. Jev on One Screen / 一屏认识 Jev
3. Know Before You Build / 开发前必读
4. Recently Added / 最近收录
5. Official & Access / 官方与接入
6. Skills & Agents / Skills 与 Agent
7. Developer Ecosystem / 开发生态
8. Patterns & Cookbook / 模式与实践
9. Projects by Use Case / 按场景浏览项目
10. Playgrounds & Reproducible Demos / 演示与复现
11. Benchmarks & Evidence / 评测与证据
12. Failures & Limitations / 失败实践与局限
13. Learn / 学习资料
14. Open Alternatives / 开源替代
15. Ecosystem Radar / 生态雷达
16. Contributing / 参与贡献

## 第一部分：Run Jev Now / 立即体验

该部分位于目录之后，为首次访问者提供三条最短路径：

1. **在线体验**：无需本地安装的官方或可信 Playground。
2. **第一次 API 调用**：官方直连或当前可用网关的最小 Python、TypeScript、curl 入口。
3. **安装 Agent Skill**：官方 Skill 的安装命令，以及支持的 Agent 范围。

每条路径使用统一字段：

- 适合谁
- 前置条件
- 开始方式
- 预计耗时
- 来源与验证状态

本节不重复完整教程，只提供最短可执行入口，并链接到后续的官方资源、Skills 和 Cookbook 栏目。

## 非目标

- 首次交付不建设独立网站、搜索、排行榜或自动采集系统。
- 不在 `Run Jev Now` 中堆叠全部 SDK 和社区客户端。
- 不复述未经核查的性能、准确率或“零幻觉”营销结论。
- 不将普通分类器或仅模仿 Jev 接口的项目混入 Jev 核心生态。

## 验收标准

- 两个 README 的目录结构一致，锚点可用。
- 第一部分至少提供在线体验、API 调用、Agent Skill 三条路径。
- 所有命令来自官方文档或官方仓库，并在写入前重新核查。
- 所有外链可访问，并标注官方或社区来源。
- 中文表达自然，英文不是逐字硬译。
