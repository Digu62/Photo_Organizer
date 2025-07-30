import os
import shutil
from datetime import datetime
from PIL import Image

import tkinter as tk
from tkinter import filedialog

from configs.config import logger

class PhotoOrganizer():
    extensions = ['jpg','jpeg','JPG','JPEG', 'png']

    def __init__(self):
        logger.info("Buscando definição da pasta origem.")
        origin = self.get_origin_path()
        logger.debug(f"Pasta origem selecionada: {origin}")
        destination = self.get_destination_path()
        logger.debug(f"Pasta destino selecionada: {destination}")
        self.origin = origin
        self.destination = destination

    def get_path_to_move(self, file_path):
        """Define o caminho para a pasta onde a foto será movida com base
        na data da foto.

        Args:
            file_path (str): Caminho para a imagem.

        Returns:
            str: Caminho da pasta onde a foto será movida.
        """
        logger.info(f"Definindo caminho da imagem: {file_path}")
        date = self.get_image_date(file_path)
        months = {
            '01': 'Janeiro',
            '02': 'Fevereiro',
            '03': 'Março',
            '04': 'Abril',
            '05': 'Maio',
            '06': 'Junho',
            '07': 'Julho',
            '08': 'Agosto',
            '09': 'Setembro',
            '10': 'Outubro',
            '11': 'Novembro',
            '12': 'Dezembro'
        }
        actual_month = date.strftime("%m")
        month_number = months.get(actual_month, 'Mês Desconhecido')
        path = date.strftime('%Y' + '/' + month_number)
        destination = os.path.join(self.destination, path)
        logger.info(f"Destino definido como: {destination}")
        return destination


    def get_image_date(self, file_path):
        """Captura a data da imagem com base nos metadados ou modificação.

        Args:
            file_path (str): Caminho para a imagem.

        Returns:
            datetime: Data da imagem.
        """
        photo = Image.open(file_path)
        logger.info(f"Capturando data da imagem: {file_path}")
        date = None
        logger.info(f"Photo exif: {photo.getexif()}")
        if not photo.getexif() == {}:
            info = photo._getexif()
            if 36867 in info:
                date = info[36867]
                date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        if date is None:
            #TODO Validar se é coerente usar essa operação na organização
            logger.warning(f"Metadados não encontrados, definindo por data de modificação.")
            date = datetime.fromtimestamp(os.path.getmtime(file_path))
        logger.info(f"Data da imagem {file_path}: {date}")
        return date

    def move_image(self, file_path):
        """Move a imagem para a pasta definida com base na data.

        Args:
            file_path (str): Caminho para a imagem.
        """
        
        folder = self.get_path_to_move(file_path)
        if not os.path.exists(folder):
            logger.info(f"Criando pasta: {folder}")
            os.makedirs(folder)
        logger.info(f"Movendo imagem para pasta: {folder}")
        final_path = os.path.join(folder, os.path.basename(file_path))
        logger.debug(f"Caminho criado: {final_path}")
        shutil.move(file_path, final_path)

    def get_origin_path(self):
        """Seleciona a pasta onde as fotos estão localizadas.

        Returns:
            str: Caminho para a pasta
        """
        logger.info("Abrindo seletor de pasta.")
        root = tk.Tk()
        root.withdraw()  # Oculta a janela principal
        caminho = filedialog.askdirectory(title="Selecione a pasta de fotos")
        logger.info(f"Pasta selecionada: {caminho}")
        return caminho
    
    def get_destination_path(self):
        """Seleciona a pasta onde as fotos serão organizadas.

        Returns:
            str: Caminho para a pasta
        """
        logger.info("Abrindo seletor de pasta.")
        root = tk.Tk()
        root.withdraw()  # Oculta a janela principal
        caminho = filedialog.askdirectory(title="Selecione a pasta destino")
        logger.info(f"Pasta selecionada: {caminho}")
        return caminho

    def organize(self):
        """Seleciona as imagens no diretório atual e as move para as pastas
        correspondentes com base na data da imagem.
        """
        logger.info("Iniciando organização de fotos.")
        logger.debug(f"Procurando por arquivos com extensões: {self.extensions}")
        try:
            logger.debug(f"Files: {os.listdir(self.origin)}")
            photos = [
                filename for filename in os.listdir(self.origin) if any(filename.endswith(ext) for ext in self.extensions)
            ]
            if photos:
                for filename in photos:
                    if self.origin:
                        filename = os.path.join(self.origin, filename)
                    self.move_image(filename)
                logger.info("Organização de fotos concluída.")
            else:
                logger.warning("Nenhuma foto encontrada para organizar.")
        except Exception as e:
            logger.error(f"Erro ao organizar fotos: {e}")
            raise e

PO = PhotoOrganizer()
PO.organize()