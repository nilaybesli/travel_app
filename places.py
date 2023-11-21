from flask import Flask,jsonify

app = Flask(__name__)


places= [{
        "id": 1,
        "name": "Machu Picchu",
        "description": "Machu Picchu is known as the mysterious city of the Inca Empire. Located in the Andes Mountains in Peru, this ancient city offers breathtaking views.",
        "price": 1200,
        "stars": 8,
        "people": 250,
        "selected_people": 0,
        "img": "https://cdn.mos.cms.futurecdn.net/WFJBpzs4J5x3uvbeKdnm3i-1200-80.jpg",
        "location": "Cusco, Peru"
      },
      {
        "id": 2,
        "name": "Petra",
        "description": "Petra is an ancient city hidden in the desert landscape of Jordan. It is famous for its magnificent rock carvings and historical ruins.",
        "price": 1000,
        "stars": 4,
        "people": 200,
        "selected_people": 0,
        "img": "https://media.istockphoto.com/id/1170941515/tr/foto%C4%9Fraf/al-khazneh-petra-i%C3%A7inde.jpg?s=612x612&w=0&k=20&c=1S267PK-fDpCPPhawdCqBxjTwsQMk73iuN2X873Us7s=",
        "location": "Ma'an, Jordan"
      },
      {
        "id": 3, 
        "name": "Great Wall of China",
        "description": "The Great Wall of China is known as the world's longest wall. It protected China from invasions for thousands of years.",
        "price": 800,
        "stars": 6,
        "people": 300,
        "selected_people": 0,
        "img": "https://images.travelandleisureasia.com/wp-content/uploads/sites/3/2023/02/02192048/great-wall-of-china.jpeg?tr=w-1200,h-900",
        "location": "Beijing, China"
      },
      {
        "id": 4,
        "name": "Chichen Itza",
        "description": "Chichen Itza is famous for the remnants of the ancient Maya civilization. It is located on the Yucatan Peninsula in Mexico.",
        "price": 1100,
        "stars": 4,
        "people": 220,
        "selected_people": 0,
        "img": "https://cdn.britannica.com/86/179586-138-8B763D72/Overview-Chichen-Itza-Yucatan-Mexico.jpg",
        "location": "Yucatan, Mexico"
      },
      {
        "id": 5,
        "name": "Roman Colosseum",
        "description": "The Roman Colosseum is an iconic symbol of the ancient Roman Empire. It is known for gladiator fights and impressive architecture.",
        "price": 900,
        "stars": 7,
        "people": 280,
        "selected_people": 0,
        "img": "https://www.unescodunyamiraslari.com/wp-content/uploads/2018/08/kolezyum-roma.jpg",
        "location": "Rome, Italy"
      },
      {
        "id": 6,
        "name": "Taj Mahal",
        "description": "The Taj Mahal, located in Agra, India, is a captivating monument of love. It is famous for its white marble and beautiful gardens.",
        "price": 950,
        "stars": 5,
        "people": 260,
        "selected_people": 0,
        "img": "https://media.istockphoto.com/id/155096944/tr/foto%C4%9Fraf/taj-mahal-sunrise.jpg?s=612x612&w=0&k=20&c=b3ye-5ZSRuiQAOwy-ecr2eo7cSTLIiZX23TJsiX47DM=",
        "location": "Agra, India"
      },
      {
        "id": 7,
        "name": "Amazon Rainforest",
        "description": "The Amazon Rainforest is the world's largest rainforest. Known for its unique biodiversity, it extends along the Amazon River in Brazil.",
        "price": 1300,
        "stars": 4,
        "people": 320,
        "selected_people": 0,
        "img": "https://images.nationalgeographic.org/image/upload/v1638890315/EducationHub/photos/amazon-river-basin.jpg ",
        "location": "Manaus, Brazil"
      }
    ]


@app.route('/getplaces')
def hello_world():

    return places 

if __name__ == '__main__':
    app.run(debug=True)
    
