import requests

url = 'https://api.thecatapi.com/v1/images/search'


for i in range(10):
    r = requests.get(url)
    if r.ok:
        x = r.json()

        print(x[0]['url'])
        # Het gebruikt van stream is niet essentieel, maar zeker wel aan te raden voor bestanden groter dan een paar kilobyte.
        image = requests.get(x[0]['url'], stream=True)

        if image.ok:
            # Op deze manier een bestand openen zorgt er ook meteen voor dat deze automatisch wordt gesloten. Dit maakt het veiliger om met files te werken.
            with open(x[0]['url'].split('/')[-1], 'wb') as f:
                # image.content is automatisch een byte string
                # f.write schrijft in één keer alles weg, mogelijk strookt dit tegen de stream methode in
                f.write(image.content)
        else:
            print("Failed to download image")
    else:
        print("Failed to GET from API")
