from flask import Flask,jsonify,request
app=Flask(__name__)
@app.route('/add/',methods=["POST","GET"])
def add():
    if not "a" in request.values or not "b"  in request.values:
        return jsonify({"code":"1001","msg":"请求参数缺失"})
    a=request.values.get("a")
    b=request.values.get("b")
    sum=float(a)+float(b)
    return jsonify({"code":"10000","msg":"成功","result":a})
@app.route("/api/sub",methods=["POST"])
def subt():
    if not request.json:
        return jsonify({"code":"10002","msg":"请求参数类型错误"})
    if not "a" in request.json or not "b" in request.json:
        return jsonify({"code":"10001","msg":"请求参数缺少值"})
    a=request.json.get("a")
    b=request.json.get("b")
    result=float(a)-float(b)
    return jsonify({"code":"10000","msg":"成功","result":result})
if __name__=="__main__":
    app.run(port=5006)