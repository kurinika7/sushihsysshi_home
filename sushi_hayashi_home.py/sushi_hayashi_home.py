import streamlit as st
import streamlit.components.v1 as components

# ✅ ページ設定（最初に記述）
st.set_page_config(page_title="鮨 はやし", layout="centered")

# ✅ 書籍風スタイル（白背景＋明朝体）
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Shippori+Mincho&display=swap');

html, body, [class*="css"] {
    font-family: 'Shippori Mincho', serif;
    font-size: 17px;
    line-height: 1.8;
    background-color: #ffffff;
    color: #000000;
}

.block-container {
    max-width: 700px;
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
    padding-left: 1rem;
    padding-right: 1rem;
    margin: auto;
}

h1, h2, h3 {
    margin-bottom: 0.3rem;
    margin-top: 2rem;
}

iframe {
    margin-top: -10px;
}

/* モバイル向け調整 */
@media screen and (max-width: 600px) {
    .block-container {
        padding: 0.5rem 0.8rem;
    }
    h1, h2, h3 {
        font-size: 1.2rem;
    }
    p, li {
        font-size: 0.95rem;
    }
}
</style>
""", unsafe_allow_html=True)


# ✅ メイン画像
st.image("IMG_5204.jpg", use_column_width=True)

# ✅ メニュー紹介
st.header("おまかせコース")
st.markdown("""
- **夜のコース　¥13200税込** 
- **ランチ握り　¥5500税込**
""")

# ✅ 店舗情報
st.header("店舗情報")
st.markdown("""
**住所：** 〒420-0839 静岡県静岡市葵区鷹匠2-9-11  
**電話番号：** 080-8061-6593  
**営業時間：** 火〜土 12:00〜14:00 / 18:00〜22:00  
**定休日：** 日曜日  
**Web予約：** [TableCheckで予約する](https://www.tablecheck.com/ja/shops/sushihayashi/reserve)
""")

# ✅ Googleマップ
st.header("アクセス")
st.markdown("""
[Googleマップで開く](https://www.google.com/maps?q=〒420-0839+静岡県静岡市葵区鷹匠2-9-11 鮨はやし)
""")

# ✅ Instagram埋め込み
st.header("Instagram")
st.markdown("最新の様子はInstagramでご覧下さい：")
insta_html = """
<iframe src="https://www.instagram.com/sushihayashi2911/embed" width="400" height="480" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
<p><a href="https://www.instagram.com/sushihayashi2911/" target="_blank">▶ Instagramを開く</a></p>
"""
components.html(insta_html, height=550)

# ✅ フッター
st.markdown("---")
st.caption("© 2025 鮨 はやし")
