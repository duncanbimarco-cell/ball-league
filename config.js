/* ===== 部署配置：改成你自己的 GitHub 仓库 ===== */
window.APP_CONFIG = {
  // GitHub 用户名（或组织名）
  owner: "duncanbimarco-cell",
  // 仓库名
  repo: "ball-league",
  // 分支名（GitHub Pages 一般用 main）
  branch: "main",
  // 数据文件路径
  dataPath: "data/matches.json",
  // 组委会/裁判录入口令（改这里即可，改完重新推送一次）
  adminCode: "2026",
  // 积分规则：胜3 平1 负0
  points: { win: 3, draw: 1, lose: 0 },
  // 联赛标题
  title: "初一年级班级球类联赛",
};
