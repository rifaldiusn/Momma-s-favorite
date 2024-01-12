from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/sign-up", methods=["POST"])
def sign_up():
    data = request.get_json()

    return jsonify(data), 201

@app.route("/input-data", methods=["POST"])
def input_data():
    data = request.get_json()

    return jsonify(data), 201

@app.route("/input-goals", methods=["POST"])
def input_goals():
    data = request.get_json()

    return jsonify(data), 201

@app.route("/input-custom", methods=["POST"])
def input_custom():
    data = request.get_json()

    return jsonify(data), 201

@app.route("/results/<user_login>")
def results(user_login):
    if user_login == "Re457":
        nama = "Putra"
        umur = 32
        kelamin = "Pria"
        pekerjaan = "Dokter"
        gaji = 12000000
        
    else: 
        nama = "Putri"
        umur = 33
        kelamin = "Wanita"
        pekerjaan = "Pekerja Kantor"
        gaji = 15000000

    data = {
        "user_id:": user_login,
        "name :": nama,
        "age :": umur,
        "gender :": kelamin,
        "job :": pekerjaan,
        "salary :": gaji
        }

    output = request.args.get("results")
    if output :
        data["results"] = output
    return jsonify (data), 200


if __name__ == "__main__":
    app.run(debug=True)