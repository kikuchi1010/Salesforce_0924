# Create a Python script that generates a responsive, inline-CSS HTML file
html_content = r"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Pardot（Account Engagement）スライド</title>
<style>
  /* ========= 基本レイアウト（インラインCSS：このファイル内完結） ========= */
  :root{
    --brand:#1d307d;
    --text:#1a1a1a;
    --bg:#ffffff;
    --panel:#f7f8fb;
    --card:#ffffff;
    --border:#dfe3ea;
  }
  *{box-sizing:border-box;}
  body{
    margin:0;
    color:var(--text);
    font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,"Noto Sans JP","Hiragino Kaku Gothic ProN","Hiragino Sans",Meiryo,sans-serif;
    background:var(--bg);
    line-height:1.7;
  }

  /* 上下の余白（ページ外側） */
  .page-wrap{
    max-width: 1280px;
    margin: 48px auto;          /* ← 上下の余白 */
    padding: 0 20px;
  }

  /* 16:9 スライドの比率を保ちつつレスポンシブに拡大縮小 */
  .slide{
    width: 100%;
    aspect-ratio: 16 / 9;       /* 1920×1080 を基準に比率固定 */
    background: var(--panel);
    border: 2px solid var(--border);
    border-radius: 16px;
    padding: clamp(16px, 3vw, 40px);
    display:flex;
    flex-direction:column;
    gap: clamp(16px, 2.5vw, 28px);
    box-shadow: 0 8px 18px rgba(0,0,0,.05);
  }

  /* タイトル */
  .slide h2{
    margin:0;
    color: var(--brand);
    font-weight: 800;
    text-align: center;
    font-size: clamp(22px, 3vw, 42px); /* 1920幅では ≒42px */
    letter-spacing: .02em;
  }

  /* ボディ領域 */
  .slide .content{
    flex:1;
    display:grid;
    gap: clamp(16px, 2vw, 28px);
  }

  /* カード（ボックス） */
  .card{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: clamp(14px, 2vw, 24px);
  }
  .card h3{
    margin: 0 0 .6em 0;
    color: var(--brand);
    font-size: clamp(16px, 2.1vw, 26px);
    font-weight: 700;
  }
  .card p, .card li{
    font-size: clamp(14px, 1.4vw, 22px);
  }
  ul{margin:0; padding-left: 1.1em;}

  /* スピーカーノート */
  .note{
    background: #eef3fc;
    border: 1px solid #d6e0fb;
    border-radius: 12px;
    padding: clamp(12px, 1.8vw, 22px);
    font-size: clamp(12px, 1.3vw, 20px);
  }
  .note strong{color:#314ea0;}

  /* ========== スライド別のグリッド構成 ========== */
  /* Slide 1: 2×2 グリッド（大画面）、中画面は2列、小画面は1列 */
  .grid-2x2{
    grid-template-columns: repeat(2, 1fr);
  }

  /* Slide 2: 3カラム → 2カラム → 1カラムの順で折り返し */
  .grid-3{
    grid-template-columns: repeat(3, 1fr);
  }

  /* ========== ブレークポイント ========== */
  @media (max-width: 1200px){
    .page-wrap{margin:36px auto;}
  }
  @media (max-width: 1024px){
    .grid-2x2{ grid-template-columns: repeat(2, 1fr); }
    .grid-3{   grid-template-columns: repeat(2, 1fr); }
  }
  @media (max-width: 720px){
    .page-wrap{margin:24px auto;}
    .grid-2x2{ grid-template-columns: 1fr; }
    .grid-3{   grid-template-columns: 1fr; }
  }

  /* ========== 1920×1080での静的出力（任意利用） ==========
     もし正確な 1920×1080 PNG/JPG でのキャプチャを想定する場合は、
     このクラスを最上位コンテナに付与してください（例：<div class="page-wrap fixed-1920">）。 */
  .fixed-1920 .slide{
    width: 1920px;
    height: 1080px;
    aspect-ratio: auto; /* 固定サイズ優先 */
    padding: 40px;
  }
</style>
</head>
<body>
  <div class="page-wrap">

    <!-- ========== Slide 1 ========== -->
    <section class="slide" role="region" aria-label="Pardot スライド 1">
      <h2>Pardot（Account Engagement）とは・役割・機能・メリット</h2>

      <div class="content grid-2x2">
        <!-- Pardotとは -->
        <div class="card">
          <h3>Pardotとは</h3>
          <ul>
            <li>Salesforceが提供する<strong>B2B向けマーケティングオートメーション（MA）ツール</strong></li>
            <li>見込み顧客の獲得・育成・営業連携を効率化</li>
            <li>現在は「Account Engagement」として提供</li>
          </ul>
        </div>

        <!-- 基本的な役割 -->
        <div class="card">
          <h3>基本的な役割</h3>
          <ul>
            <li><strong>リード獲得</strong>：WebフォームやLPで見込み顧客情報を収集</li>
            <li><strong>リードナーチャリング</strong>：メール配信やスコアリングで関心度を高める</li>
            <li><strong>リードスコアリング</strong>：行動を点数化し、有望顧客を営業に渡す</li>
            <li><strong>レポーティング</strong>：施策効果を測定（開封率、クリック率、CV率など）</li>
          </ul>
        </div>

        <!-- 主な機能 -->
        <div class="card">
          <h3>主な機能</h3>
          <ul>
            <li><strong>メールマーケティング</strong>：セグメント配信、パーソナライズ、A/Bテスト</li>
            <li><strong>LP／フォーム作成</strong>：ノーコード作成、Salesforceへ自動連携</li>
            <li><strong>リード管理</strong>：スコア（行動）＋グレード（属性）で有望リードを特定</li>
            <li><strong>キャンペーン連携</strong>：商談データと結合し売上貢献を可視化</li>
          </ul>
        </div>

        <!-- メリット -->
        <div class="card">
          <h3>メリットと活用ポイント</h3>
          <ul>
            <li><strong>営業部門とマーケ部門の連携がスムーズ</strong> → 有望顧客だけを営業に渡せるため、商談化率UP</li>
            <li><strong>B2B向けの長期的な顧客育成に強い</strong> → 高額商材や長期検討プロセスを伴う業界に最適</li>
            <li><strong>Salesforce CRMとシームレスに統合</strong> → 顧客情報を一元管理し、営業活動の精度を高められる</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- ========== Slide 2 ========== -->
    <section class="slide" role="region" aria-label="Pardot スライド 2">
      <h2>課題・業務の流れ・目先の実施事項</h2>

      <div class="content grid-3">
        <!-- 課題 -->
        <div class="card">
          <h3>課題</h3>
          <ul>
            <li>Pardotはマーケティングで活用中</li>
            <li>データは取得できているが、今後は<strong>営業効率化</strong>や<strong>営業ツール</strong>としてどう活用するか検討が必要</li>
          </ul>
        </div>

        <!-- 業務の流れ -->
        <div class="card">
          <h3>業務の流れ</h3>
          <p style="margin:0; font-size: clamp(14px, 1.5vw, 22px);">
            依頼者 <span style="color:var(--brand);">→</span> 髙橋（外部Salesforceベンダー）：こちらで実装
            <span style="color:var(--brand);">→</span> 確認：JMJ / CE：谷口さん
          </p>
        </div>

        <!-- 目先の実施事項 -->
        <div class="card">
          <h3>目先の実施事項</h3>
          <ul>
            <li>坂口さんから<strong>営業アタックリスト</strong>に関して共有・推進が必要</li>
          </ul>
        </div>
      </div>

      <!-- スピーカーノート -->
      <div class="note" aria-label="スピーカーノート">
        <strong>発表者コメント（スピーカーノート用解説）</strong><br/>
        ・課題：現在はPardotをマーケティング施策中心に使っているが、営業にどう還元するかが次の検討ポイント。<br/>
        ・業務の流れ：依頼者から外部ベンダーの髙橋さんが実装を行い、その後、JMJ/CEの谷口さんが確認するフロー。<br/>
        ・目先の実施事項：まずは坂口さんと連携し、<strong>営業アタックリスト</strong>を整理・共有して推進する。
      </div>
    </section>

  </div>
</body>
</html>
"""

# Write both the generator script and the output HTML
py_code = r'''# build_pardot_slides.py
# 使い方: `python build_pardot_slides.py` を実行すると pardot_slides.html を出力します。

html = """REPLACE_HTML"""
with open("pardot_slides.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Wrote pardot_slides.html")
'''
# Save files
with open("/mnt/data/pardot_slides.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("/mnt/data/build_pardot_slides.py", "w", encoding="utf-8") as f:
    f.write(py_code.replace("REPLACE_HTML", html_content.replace('"""','\\"\"\\"')))

"Files created: pardot_slides.html and build_pardot_slides.py"
