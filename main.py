from flask import Flask, request

app = Flask(__name__)


@app.route('/phones/create/')
def create_phone():
    import sqlite3
    con = sqlite3.connect('example.db')

    # http://127.0.0.1:5001/phones/create/?contactName=Vika&Phone=380939716012
    contact_name = request.args['contactName']
    phone_value = request.args['Phone']

    cur = con.cursor()
    sql_query = f'''
        INSERT INTO phones (contactName, phoneValue)
        VALUES ('{contact_name}', '{phone_value}');
        '''
    cur.execute(sql_query)

    con.commit()
    con.close()
    return 'create_phone'


@app.route('/phones/read/')
def read_phone():
    import sqlite3
    con = sqlite3.connect('example.db')

    cur = con.cursor()
    sql_query = f'''
    SELECT * FROM phones;
    '''
    cur.execute(sql_query)
    result = cur.fetchall()
    con.close()
    return str(result)


@app.route('/phones/update/')
def update_phone():
    import sqlite3
    con = sqlite3.connect('example.db')

    # http://127.0.0.1:5001/phones/update/?contactName=Vika&Phone=380939716012
    contact_name = request.args['contactName']
    phone_value = request.args['Phone']

    cur = con.cursor()
    sql_query = f'''
    UPDATE phones
    SET contactName = '{contact_name}' 
    WHERE phoneValue = '{phone_value}';
        '''
    cur.execute(sql_query)

    con.commit()
    con.close()
    return 'update_phone'


@app.route('/phones/delete/')
def delete_phone():
    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    sql_query = f'''
    DELETE FROM phones;
    '''
    cur.execute(sql_query)
    con.commit()
    con.close()
    return 'delete_phone'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
