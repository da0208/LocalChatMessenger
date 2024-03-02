# LocalChatMessenger

## 概要
RecursionのバックエンドプロジェクトでのPythonのソケット通信とfakerパッケージを使用した、クライアントサーバ間で情報をやり取りするシンプルなアプリケーション


## 機能
・　クライアント側: 指定されたホストとポートに接続し、接続が確定するとユーザからの入力('->'で示される)をサーバに送信します。ユーザが'bye'と入力すると接続が閉じます。

・　サーバ側: クライアントからの接続を受け入れ、アドレスを表示します。その後、クライアントからのデータを受信し表示します。そして、Fakerライブラリを使用して生成されたランダムな文章をクライアントに送信します。
