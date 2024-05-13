import csv
import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDefaultSuite():
    def read_input_from_csv(self, filename):
        input_data = []
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                input_data.append(row)
        return input_data

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_with_input_from_csv(self):
        input_filename = "./input.csv"
        output_filename = "./output.csv"  # Chemin du fichier de sortie

        input_data = self.read_input_from_csv(input_filename)
        output_data = []

        for row in input_data:
            email = row[0]
            password = row[1]

            self.driver.get("http://localhost:3000/login")
            self.driver.set_window_size(974, 1032)
            self.driver.find_element(By.NAME, "name").click()
            self.driver.find_element(By.NAME, "name").send_keys(email)
            self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").click()
            self.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) > .rounded-3xl").send_keys(password)
            self.driver.find_element(By.CSS_SELECTOR, ".bg-\\[\\#4A7B59\\]").click()

            # Vérifier si la connexion a réussi en vérifiant l'URL actuelle
            if self.driver.current_url == "http://localhost:3000/":
                status = "KO"
            else:
                status = "OK"

            output_data.append([email, password, status])

            # Pause pour observer les résultats
            time.sleep(5)

        # Créer le répertoire de sortie s'il n'existe pas déjà
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)

        # Écrire les résultats dans le fichier de sortie
        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Email', 'Password', 'Status'])
            writer.writerows(output_data)

if __name__ == "__main__":
    pytest.main([__file__])
