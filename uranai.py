import time
import random
import IPython
from google.colab import output


n = 0 
def chat(text, **kw):  #チャット用の関数（ここを書き換える）
  global n
  n += 1
  return 'ほ' * n


# アイコンの指定
BOT_ICON = "https://img.icons8.com/external-victoruler-flat-victoruler/64/000000/external-lizard-animal-squad-victoruler-flat-victoruler.png"
YOUR_ICON = 'https://img.icons8.com/color/64/000000/frog.png'

def run_chat(chat = chat, start='あなたのことを占ってもいいかい？', **kw):
  display(IPython.display.HTML(f'''
  <div class="head">
    <h3>リザードくん</h3>
  </div>
  '''))

  def display_bot(bot_text):
    with output.redirect_to_element('#output'):
      bot_name = kw.get('bot_name', 'リザードくん')
      bot_icon = kw.get('bot_icon', BOT_ICON)
      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-left">
            <img src="{bot_icon}" width="60px">
        </div><!-- /.icon-img icon-img-left -->
        <div class="icon-name icon-name-left">{bot_name}</div>
        <div class="sb-side sb-side-left">
            <div class="sb-txt sb-txt-left">
              {bot_text}
            </div><!-- /.sb-txt sb-txt-left -->
        </div><!-- /.sb-side sb-side-left -->
    </div><!-- /.sb-box -->
      '''))

  def display_you(your_text):
    with output.redirect_to_element('#output'):
      your_name = kw.get('your_name', 'あなた')
      your_icon = kw.get('your_icon', YOUR_ICON)

      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-right">
            <img src="{your_icon}" width="60px">
        </div><!-- /.icon-img icon-img-right -->
        <div class="icon-name icon-name-right">{your_name}</div>
        <div class="sb-side sb-side-right">
            <div class="sb-txt sb-txt-right">
              {your_text}
            </div><!-- /.sb-txt sb-txt-right -->
        </div><!-- /.sb-side sb-side-right -->
      </div><!-- /.sb-box -->
      '''))

  display(IPython.display.HTML('''

      <style>
        /* ヘッダー */
        .head{
          background-color:#d3c496;
          border-bottom:2px solid #afa07f;
          padding-left:50px;
          padding-top:5px;
          padding-bottom:10px;

        }
        h3{
          font-size:25px;
          color:#6e5064;
          font-family:"Yu Gothic", "游ゴシック", YuGothic, "游ゴシック体";
          

        }


        /* 全体 */
        .sb-box {
            background-color:#bdc6b7;
            padding-top:15px;
            padding-bottom:10px;
            position: relative;
            overflow: hidden;
        }

        /* アイコン画像 */
        .icon-img {
            position: absolute;
            overflow: hidden;
            top: 0;
            width: 80px;
            height: 80px;
        }

        /* アイコン画像（左） */
        .icon-img-left {
            margin-top:20px;
            margin-left:20px;
            left: 0;
        }

        /* アイコン画像（右） */
        .icon-img-right {
            margin-right:10px;
            right: 0;
        }

        /* アイコン画像 */
        .icon-img img {
            border-radius: 50%;
            border: 2px solid #eee;
        }

        /* アイコンネーム */
        .icon-name {
            position: absolute;
            width: 80px;
            text-align: center;
            top: 83px;
            color: #fff;
            font-size: 11px;
        }

        /* アイコンネーム（左） */
        .icon-name-left {
            margin-left:15px;
            margin-top:10px;
            left: 0;
        }

        /* アイコンネーム（右） */
        .icon-name-right {
          margin-right:15px;
          margin-top:3px;
            right: 0;
        }

        /* 吹き出し */
        .sb-side {
            position: relative;
            float: left;
            margin: 0 105px 40px 105px;
        }

        .sb-side-right {
            float: right;
        }

        /* 吹き出し内のテキスト */
        .sb-txt {
            position: relative;
            border: 2px solid #eee;
            border-radius: 15px;
            background: #eee;
            color:#6e5064;
            /* font-family:"Yu Gothic", "游ゴシック", YuGothic, "游ゴシック体";
            font-wegiht:5px; */
            font-size: 17px;
            line-height: 1.7;
            padding:5px;
            padding-right:8px;
            padding-left:8px;
        }

        .sb-txt>p:last-of-type {
            padding-bottom: 0;
            margin-bottom: 0;
        }

        /* 吹き出しの三角 */
        .sb-txt:before {
            content: "";
            position: absolute;
            border-style: solid;
            top: 16px;
            z-index: 3;
        }

        .sb-txt:after {
            content: "";
            position: absolute;
            border-style: solid;
            top: 15px;
            z-index: 2;
        }

        /* 吹き出しの三角（左） */
        .sb-txt-left:before {
            left: -7px;
            
            border-width: 7px10px 7px 0;
            border-color: transparent #eee transparent transparent;
        }

        .sb-txt-left:after {
            left: -10px;
            border-width: 8px 10px 8px 0;
            border-color: transparent #eee transparent transparent;
        }

        /* 吹き出しの三角（右） */
        .sb-txt-right:before {
            right: -7px;
          
            border-width: 7px 0 7px 10px;
            border-color: transparent transparent transparent #eee;
        }

        .sb-txt-right:after {
            right: -10px;
            border-width: 8px 0 8px 10px;
            border-color: transparent transparent transparent #eee;
        }

        /* 767px（iPad）以下 */

        @media (max-width: 767px) {

            .icon-img {
                width: 60px;
                height: 60px;
            }

            /* アイコンネーム */
            .icon-name {
                width: 60px;
                top: 62px;
                font-size: 9px;
            }

            /* 吹き出し（左） */
            .sb-side-left {
                margin: 0 0 30px 78px;
                /* 吹き出し（左）の上下左右の余白を狭く */
            }

            /* 吹き出し（右） */
            .sb-side-right {
                margin: 0 78px 30px 0;
                /* 吹き出し（右）の上下左右の余白を狭く */
            }

            /* 吹き出し内のテキスト */
            .sb-txt {
                padding: 12px;
                /* 吹き出し内の上下左右の余白を-6px */
            }
        }
    </style>
      <script>
        var inputPane = document.getElementById('input');
        inputPane.addEventListener('keydown', (e) => {
          if(e.keyCode == 13) {
            google.colab.kernel.invokeFunction('notebook.Convert', [inputPane.value], {});
            inputPane.value=''
          }
        });
      </script>
    <div id='output' style='background: #66d;'></div>
    <div style='text-align: right'><textarea id='input' style='width: 100%; background: #eee;'></textarea></div>
      '''))

  def convert(your_text):
    display_you(your_text)
    bot_text = chat(your_text, **kw)
    time.sleep(random.randint(0,4))
    display_bot(bot_text)

  output.register_callback('notebook.Convert', convert)
  if start is not None:
    display_bot(start)

frame = {}

def myuranai(input_text):
  global frame # 外部の状態を参照する
  if 'asking' in frame:  # asking から更新する
    frame[frame['asking']] = input_text
    del frame['asking']

  if 'sei' not in frame:
    frame['asking'] = 'sei' # 名前をたずねる  
    return 'あなたの性別を番号で教えて！  １．女性　２．男性　３．どちらでもない'

  if 'sei' in frame and 'birthday' not in frame:
    frame['asking'] = 'birthday' # 誕生日をたずねる    
    return '何年生まれか教えて！'

  if 'sei' in frame and 'birthday' in frame:
    
    # 占います
    number = int(frame['birthday'])
    if number < 1950:
      return '☆ラッキーアクション☆毎朝10分散歩すると、運気が上がるよ。'
    elif number >= 1950 and number <= 1964:
      return '☆ラッキーアクション☆朝にトイレ掃除をすると、運気が上がるよ。'
    elif number >= 1965 and number <= 1984:
      return '☆ラッキーアクション☆朝に5分間だけストレッチしてみると、運気が上がるよ。'
    elif number >= 1985 and number <= 1994:
      return '☆ラッキーアクション☆アロマを焚いて寝ると、運気があがるよ。'
    elif number >= 1995:
      return '☆ラッキーアクション☆朝に5分間読書をすると、運気が上がるよ。'
    

  return output_text

def start():
  run_chat(chat=myuranai)    
