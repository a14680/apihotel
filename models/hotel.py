class HotelModel:
    def __init__(self,hotel_id,estrelas,diaria,cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
                "Hotel_id": self.hotel_id,
                "nome": self.nome,
                "estrelas": self.estrelas,
                "diaria": self.diaria,
                "cidade": self.cidade
            }
