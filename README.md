# はじめに
* API Gateway + Lambda(Python) のサンプルコード
* python-lambda-local と lambda-uploader を利用してローカル開発

# 利用手順
## 事前準備
### Python環境構築（構築済の場合不要）

```python
$ brew install pyenv 
$ pyenv install 3.7.4 
$ pyenv global 3.7.4 
$ mkdir -p ~/opt/python_env 
$ cd python_env; pwd 
# 上記でセットアップしたpythonを利用
$ python -m venv py374env 
$ source /Users/username/opt/python_env/py374env/bin/activate 
$ pip install numpy 
$ pip install Pillow 
$ pip install jupyter 
$ jupyter notebook --notebook-dir=~/pj/ & 
```

### python-lambda-local と lambda-uploader のインストール

```bash
$ pip install python-lambda-local lambda-uploader
```

### API GateWayの作成
* HTTP API
* 統合
    * Lambda
* ルート
    * POST /lambda_api_test → lambda_api_test (Lambda)
* ステージ
    * $default (Auto-deploy: enabled)

### IAMユーザ作成
* Lambdaアップロード用
  * aws configure で設定しておく
* Lambda実行用
  * lambda.json （後述）で設定する

## 開発
* フォルダ構成

```bash
lambda_api_test/
├── event.json
├── lambda.json
├── lambda_function.py
└── requirements.txt
```

* lambda.json
  * roleにLambda実行用のロールを設定する

## 実行
* ローカルでのテスト

```bash
$ python-lambda-local -f lambda_handler lambda_function.py event.json
```

* アップロード

```bash
$ lambda-uploader
```

* テスト
```
$ curl -X POST -H "Content-Type: application/json" -d '{"a":2, "b":3}' https://<MY_URL>/lambda_api_test
```

## 追加設定
### セキュリティ設定
* 非VPCの場合
    * [リソースポリシーを使用して特定の IP アドレスをホワイトリストに登録し、API Gateway API にアクセスする方法を教えてください。](https://aws.amazon.com/jp/premiumsupport/knowledge-center/api-gateway-resource-policy-whitelist/)
* VPCの場合
  * [[新機能] Amazon API GatewayプライベートAPIとVPCエンドポイントでプライベートなサーバーレスアプリ構築](https://dev.classmethod.jp/articles/apigateway-supports-vpc-endpoint/)
    * Amazon API GatewayプライベートAPIとVPCエンドポイントを利用して、VPCやDirect Connectにサーバーレスアプリを提供する
      * VPCサブネット(基本的には全部選択)およびセキュリティグループ(API GatewayはHTTPS:443なのでそれを許可するルール)を選択、エンドポイントを作成

# 参考
* [python-lambda-local と lambda-uploader を使ってローカル環境で Lambda 開発を行う](https://sig9.hatenablog.com/entry/2020/02/08/000000)
