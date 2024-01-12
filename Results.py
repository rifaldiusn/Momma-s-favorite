from fastapi import FastAPI

app = FastAPI()

inventory = {
    0:{
        "Jenis gaji": "bawah umr",
        "keadaan hidup": "miskin",
        "saran": "cari kerja dah lu"
    },

    1: {
        "Jenis gaji": "bawah umr",
        "keadaan hidup": "miskin",
        "saran": "cari peruntungan lain"
    },

    2:{
        "Jenis gaji": "bawah umr",
        "keadaan hidup": "miskin",
        "saran": "coba berusaha lagi"
    },

    3:{
        "Jenis gaji": "bawah umr",
        "keadaan hidup": "miskin",
        "saran": "coba berusaha lagi"
    },

    4:{
        "Jenis gaji": "umr",
        "keadaan hidup": "pas pasan",
        "saran": "coba berusaha lagi"
    },

    5:{
        "Jenis gaji": "umr",
        "keadaan hidup": "pas pasan",
        "saran": "coba berusaha lagi"
    },

    6:{
        "Jenis gaji": "umr",
        "keadaan hidup": "pas pasan",
        "saran": "coba berusaha lagi"
    },

    7:{
        "Jenis gaji": "atas umr",
        "keadaan hidup": "tercukupi",
        "saran": "tetap hemat dan jangan lupa berbagi"
    },

    8:{
        "Jenis gaji": "atas umr",
        "keadaan hidup": "tercukupi",
        "saran": "tetap hemat dan jangan lupa berbagi"
    },

    9:{
        "Jenis gaji": "atas umr",
        "keadaan hidup": "tercukupi",
        "saran": "tetap hemat dan jangan lupa berbagi"
    },

    10:{
        "Jenis gaji": "atas umr",
        "keadaan hidup": "tercukupi",
        "saran": "tetap hemat dan jangan lupa berbagi"
    }
}

@app.get("/gaji-anda/{item_id}")  
def get_item(item_id: int):
    return inventory[item_id]