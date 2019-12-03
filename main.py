from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

bd = mysql.connector.connect(host='localhost', user='kevin', passwd= '12345', database= 'proyecto')
cursor = bd.cursor()

@app.route('/contactos/', methods=["GET", "POST", "DELETE"])

def contactos():
    if request.method == "GET":
        query = "SELECT * FROM contactos"
        personas = []
        cursor.execute(query)

        for contacto in cursor.fetchall():
            d = {
                'id': contacto[0],
                'nombre': contacto[1],
                'tel': contacto[2],
                'email': contacto[3],
                'face': contacto[4],
                'twitter': contacto[5],
                'insta': contacto[6]
            }
            personas.append(d)
            # print(contacto)

        print(personas)
        return jsonify(personas)
    elif request.method == "POST":

            data = request.get_json()
            print(data)

            query = "INSERT INTO contactos(nombre, tel, email, face, twitter, insta) VALUES(%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (data['nombre'], data['tel'], data['email'], data['face'], data['twitter'], data['insta']))

            bd.commit()
            if cursor.rowcount:
                return jsonify({'data': 'Ok'})
            else:
                return jsonify({'data': 'Error'})

@app.route('/delete/', methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        data2 = request.get_json()
        print(data2)

        query = "DELETE FROM contactos WHERE id = '%s'"
        cursor.execute(query, (data2['id'],))

        bd.commit()
        if cursor.rowcount:
            return jsonify({'data2': 'Ok'})
        else:
            return jsonify({'data2': 'Error'})

@app.route('/update/', methods=["POST"])
def update():
    data = request.get_json()
    print(data)

    query = "UPDATE contactos SET nombre=%s, tel=%s, email=%s, face=%s, twitter=%s, insta=%s WHERE id = '%s'"
    cursor.execute(query, (data['nombre'], data['tel'], data['email'], data['face'], data['twitter'], data['insta'], data['id']))

    bd.commit()
    if cursor.rowcount:
        return jsonify({'data': 'Ok'})
    else:
        return jsonify({'data': 'Error'})


app.run(debug=True)