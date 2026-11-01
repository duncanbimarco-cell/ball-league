# 初一年级班级球类联赛 · 赛程积分系统

16 个班：单号班（1/3/5/7/9/11/13/15）踢足球，双号班（2/4/6/8/10/12/14/16）打篮球，各 5 轮、每队 5 场，共 40 场。
一个纯静态网页，数据存在 GitHub 仓库的 `data/matches.json` 里，扫码即可查看，**比分实时写入仓库**，不需要服务器、不需要数据库。

---

## 一、部署（做一次，10 分钟）

### 1. 建仓库
在 GitHub 新建仓库（例如 `ball-league`，**Public**），把本目录所有文件推上去：

```bash
cd ball-league
git init
git add .
git commit -m "init 班级球赛系统"
git branch -M main
git remote add origin https://github.com/<你的用户名>/ball-league.git
git push -u origin main
```

### 2. 改配置
编辑 `config.js`，把 `owner` 改成你的 GitHub 用户名、`repo` 改成仓库名：

```js
owner: "YOUR_GITHUB_NAME",   // ← 改成你的
repo:  "ball-league",
adminCode: "2026",           // 裁判录入口令，可改
```

改完再 `git commit -am "config" && git push`。

### 3. 开启 GitHub Pages
仓库 → **Settings → Pages → Source 选 `main` / 根目录 → Save**。
等待约 1 分钟，访问地址就是：

```
https://<你的用户名>.github.io/ball-league/
```

### 4. 生成 Token（给裁判设备用一次）
GitHub → 右上角头像 → **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**

- Repository access：**Only select repositories** → 选 `ball-league`
- Permissions：展开 *Repository permissions* → **Contents: Read and write**
- 生成后复制（以 `github_pat_` 开头）

---

## 二、日常使用

| 角色 | 做什么 |
|---|---|
| 学生 / 各班 | 扫码打开网页 → 看本周赛程、比分、积分榜、考勤（不用登录） |
| 裁判 / 组委会 | 打开网页 → 底部「录入」→ 输入口令 + Token → 进入录入模式 |

### 裁判录入一次比赛的流程（约 30 秒）
1. 「录入」页点这场比赛
2. 比分：点 `＋ −` 或直接点常见比分（篮球可点 20:15 / 30:20）
3. 考勤：填双方到场人数，名单可留空
4. 拍照：点「＋拍照」拍成绩表/现场照，自动压缩上传
5. 点「保存并同步」→ 全站立刻更新

### 每周赛程
- 「录入」页 → **轮次时间** → 给每轮填比赛日期 → 赛程页该轮会打上「本周」标记
- 「录入」页 → **拍照上传赛程表** → 拍下周赛程图，会显示在该轮赛程上方

### 分享二维码
「录入」页 → **生成访问二维码** → 截图打印 / 发班级群。
其他裁判设备：扫码后用 `https://…/ball-league/?token=你的Token` 打开，Token 自动存本机。

---

## 三、常见问题

- **改了数据网页没变？** 数据走 GitHub，同步要 1–2 分钟（raw 缓存）。点「录入」页的「重新拉取数据」可强制刷新。
- **照片打不开？** 新上传的照片 GitHub 需要几秒生效，稍等刷新即可。
- **积分规则** 在 `config.js` 的 `points`（默认胜 3 / 平 1 / 负 0），可改成胜 2。
- **想加比赛 / 改对阵**：直接改 `data/matches.json` 后 push，或网页上改。
- **安全**：Token 只存在录入设备本机，不进仓库；网页源码里不含密钥。口令只防手滑，不防恶意。

## 四、原表提示
赛程完全按你提供的对阵表录入（每个班每轮一场、共 5 场）。原表中存在两对重复对阵：
足球 **9班vs11班**（第1、3轮）、**7班vs13班**（第2、4轮）；
篮球 **10班vs12班**（第1、3轮）、**8班vs14班**（第2、4轮）。
如果这是笔误，告诉我要改成哪两个对手，我一键替换。
