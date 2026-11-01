import json, os

# 按原对阵表录入：单数组班(1,3,5,7,9,11,13,15)踢足球；双数组班(2,4,6,8,10,12,14,16)打篮球
FOOTBALL = {
    1: [(1, 3, "1/5号场地"), (5, 7, "2/6号场地"), (9, 11, "3/7号场地"), (13, 15, "4/8号场地")],
    2: [(1, 5, "2/6号场地"), (3, 9, "3/7号场地"), (7, 13, "4/8号场地"), (11, 15, "1/5号场地")],
    3: [(1, 7, "3/7号场地"), (3, 13, "4/8号场地"), (5, 15, "1/5号场地"), (9, 11, "2/6号场地")],
    4: [(1, 9, "4/8号场地"), (3, 15, "1/5号场地"), (5, 11, "2/6号场地"), (7, 13, "3/7号场地")],
    5: [(1, 11, "1/5号场地"), (3, 7, "2/6号场地"), (5, 13, "3/7号场地"), (9, 15, "4/8号场地")],
}

BASKETBALL = {
    1: [(2, 4, "5/1号场地"), (6, 8, "6/2号场地"), (10, 12, "7/3号场地"), (14, 16, "8/4号场地")],
    2: [(2, 6, "6/2号场地"), (4, 10, "7/3号场地"), (8, 14, "8/4号场地"), (12, 16, "5/1号场地")],
    3: [(2, 8, "7/3号场地"), (4, 14, "8/4号场地"), (6, 16, "5/1号场地"), (10, 12, "6/2号场地")],
    4: [(2, 10, "8/4号场地"), (4, 16, "5/1号场地"), (6, 12, "6/2号场地"), (8, 14, "7/3号场地")],
    5: [(2, 12, "5/1号场地"), (4, 8, "6/2号场地"), (6, 14, "7/3号场地"), (10, 16, "8/4号场地")],
}


def blank_att():
    return {"count": None, "names": ""}


matches = []
for sport, table in (("football", FOOTBALL), ("basketball", BASKETBALL)):
    prefix = "F" if sport == "football" else "B"
    for rnd in sorted(table):
        for idx, (a, b, venue) in enumerate(table[rnd], start=1):
            matches.append({
                "id": f"{prefix}{rnd}-{idx}",
                "round": rnd,
                "sport": sport,
                "a": a,
                "b": b,
                "venue": venue,
                "date": "",
                "scoreA": None,
                "scoreB": None,
                "status": "pending",
                "attA": blank_att(),
                "attB": blank_att(),
                "photos": [],
                "note": "",
            })

data = {
    "version": 1,
    "title": "初一年级班级球类联赛",
    "rounds": [{"round": i, "date": "", "label": f"第{i}轮"} for i in range(1, 6)],
    "schedulePhotos": [],
    "matches": matches,
}

out = "/Users/zhangsanmao/WorkBuddy/2026-11-01-18-06-50/ball-league/data/matches.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

fb = sum(1 for m in matches if m["sport"] == "football")
bk = sum(1 for m in matches if m["sport"] == "basketball")
print(f"总场次: {len(matches)} (足球 {fb} / 篮球 {bk})")
from collections import Counter
for sport in ("football", "basketball"):
    cnt = Counter()
    for m in matches:
        if m["sport"] == sport:
            cnt[m["a"]] += 1
            cnt[m["b"]] += 1
    print(sport, "每队场次:", sorted(cnt.items()))
    pairs = Counter(tuple(sorted((m["a"], m["b"]))) for m in matches if m["sport"] == sport)
    print(sport, "重复对阵:", [p for p, c in pairs.items() if c > 1])
