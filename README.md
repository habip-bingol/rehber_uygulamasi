# Rehber Uygulaması

Bu, Flask kütüphanesi kullanılarak oluşturulmuş basit bir rehber uygulamasıdır. Kullanıcılar, rehbere kişileri ekleyebilir, düzenleyebilir ve silebilirler.

## Başlangıç

Bu talimatlar, projenin yerel makinenizde nasıl çalıştırılacağını açıklar.

1. Sanal ortamı etkinleştirin (varsayılan olarak, venv adlı bir sanal ortam oluşturmuş olmalısınız).

    Linux/Mac:
    ```bash
    source venv/bin/activate
    ```

    Windows:
    ```bash
    venv\Scripts\activate
    ```

2. Flask uygulamasını çalıştırın.

    ```bash
    python app.py
    ```

3. Tarayıcınızda `http://127.0.0.1:5000/` adresine giderek rehber uygulamasını görüntüleyin.

## Bağımlılıklar

Projeyi çalıştırmak için aşağıdaki bağımlılığa ihtiyacınız vardır:

- Flask==2.0.1

Bağımlılıkları yüklemek için şu komutu çalıştırın:

```bash
pip install -r requirements.txt
