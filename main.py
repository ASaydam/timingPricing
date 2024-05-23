import streamlit as st
from math import floor

# Website Title
st.title("Timing Ücret Hesaplama")

# Get euro - try conversion rate
EURO = 34.8
MIN_PRICE = 250
PARTICIPANT_RATE = 0.15
ANNOUNCER = 50
LIVE_RESULT_SCREEN = 30
CERTIFICATE = 30
READER = 50
services= {
    "Sunucu": 50,
    "Canlı Sonuç Ekranı": 30,
    "Sertifika": 30,
    "Kit Dağıtım USB-Reader": 50
}
duration_options = {
    "8 saatten az": 1,
    "8-12 saat arası": 1.25,
    "12-18 saat arası": 1.50,
    "18-24 saat arası": 1.75,
    "2 gün": 2,
    "3 gün": 3
}
total = 0


def display_price(euro_price, EURO=EURO, total_calc=False):
    # Round down grand total
    if total_calc:
        return f"{floor(euro_price * 100) / 100} € ({floor(euro_price * EURO * 0.02) / 0.02} TL)"
    # Do not round low prices
    elif euro_price < 1:
        return f"{euro_price} € ({(euro_price * EURO)} TL)"
    # Rounding down everything else
    else:
        return f"{floor(euro_price * 100) / 100} € ({int(euro_price * EURO)} TL)"


def calculate_participant_price(num_participant=0):
    if num_participant <= 600:
        return 0
    else:
        return (num_participants - 600) * PARTICIPANT_RATE


# Get some race information and number of participants
event_duration = st.select_slider(
    "Etkinlik süresiniz seçiniz",
    options=list(duration_options.keys())
)
st.warning(f"Toplam ücret {duration_options[event_duration]} ile çarpılır.")

st.divider()

num_participants = st.number_input("Toplam katılımcı sayısı", min_value=0, value=0,
                                   help="Buraya ilk 600 kişi dahil toplam katılımcı sayısı giriniz.")
st.warning(f"Baz ücret: {display_price(250)}. İlk 600 katılımcı için ekstra ücret alınmaz. \n\n"
         f"600'den sonraki her katılımcı için {display_price(0.15)} eklenir")

st.divider()

# Get information about additional services
additional_services = st.multiselect(
    "Hizmetler",
    ["Sunucu", "Canlı Sonuç Ekranı", "Sertifika", "Kit Dağıtım USB-Reader"]
)


# Display price information
st.divider()
st.subheader("**Alınan Hizmetler**", divider=True)
st.write(f"Baz Ücret : {display_price(250)}")
st.write(f"Toplam {num_participants} katılımcı : {display_price(calculate_participant_price(num_participants))}")


try:
    for service in additional_services:
        st.write(f"{service}: {display_price(services[service])}")
        total += services[service]
except:
    st.write("hizmet seçiniz")


total += MIN_PRICE + calculate_participant_price(num_participants)
total *= duration_options[event_duration]

st.write(f"**Genel Toplam =** **{display_price(total, total_calc=True)}**")

st.warning("Euro kuru 34.8 TL kabul edilmiştir. Genel toplam 50 TL katına yuvarlanmıştır.")