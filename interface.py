import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from streamlit_modal import Modal
import json
import backend_functions


# les variables pour controller l'affichage

def display_head_image():
    img = Image.open("./images/money.jpg")
    st.image(img, width=100)


def space_div():
    components.html(
        """
                    <div style = "height:100px;">
                    </div>
                    """,
        height=20,
    )


def display_info_transfert():
    st.markdown(
        """
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">

        <div class="shadow bg-primary rounded pt-5 pb-5">
            <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75 rounded-top">
                <div class="form-label" style="font-weight: bold;">Agence ID</div>
                <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
            </div>
            <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75">
                <div class="form-label" style="font-weight: bold;">First Name</div>
                <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
            </div>
            <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75">
                <div class="form-label" style="font-weight: bold;">Last Name</div>
                <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
            </div>
            <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75">
                <div class="form-label" style="font-weight: bold;">Date of issue</div>
                <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
            </div>
            <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75">
                <div class="form-label" style="font-weight: bold;">Amount</div>
                <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
            </div>
            <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75">
                <div class="form-label" style="font-weight: bold;">Receiver First Name</div>
                <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
            </div>
            <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75 rounded-bottom">
                <div class="form-label" style="font-weight: bold;">Receiver Last Name</div>
                <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
            </div>
        </div>    

        """.format(agentId, firstName, lastName, date, amount, receiverFirstName, receiverLastName)
        ,
        unsafe_allow_html=True
    )


def display_title_bloc():
    components.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <div style="background-color: red">
            <div class="h2 p-3 border" style="background-color: #3286E6;color : #fff ;text-align: center;">
                ENSA GAB
            </div>
        </div>

        """,
        height=100,

    )


# les modals pour afficher les messages pop up
modal1 = Modal("Wrong Reference", key="ref")
modal2 = Modal("Wrong Pin", key="pin")
modal3 = Modal("Server error", key="err")
modal4 = Modal("Transfert Payed", key="vld")
modal5 = Modal("Empty fields", key="emp")

# debut de l'ecriture du code de la page ########################################################


display_head_image()

display_title_bloc()

columns = st.columns((1.75, 2, 1))
columns[1].markdown("# :red[GAB Menu]")

space_div()

columns_choice = st.columns((0.5, 2))
choice = columns_choice[1].radio("Please select a service", ('Consult Wallet', 'Transfert Money', 'Other Service'),
                                 horizontal=True)

space_div()

if choice == 'Other Service':

    transfert_reference = st.text_input("Enter the transfert reference", placeholder="Enter your transfert reference")
    transfert_pin = st.text_input("Enter the PIN code", placeholder="Enter your PIN code")

    space_div()

    columns_button_search = st.columns((2.25, 1, 2))

    if columns_button_search[1].button('Search'):

        if transfert_reference != "" and transfert_pin != "":
            space_div()

            transfert_searched_json = backend_functions.getTransfert(transfert_reference, transfert_pin)

            columns_infos_title = st.columns((0.65, 2, 0.15))
            columns_infos = st.columns((0.30, 2, 0.25))

            if transfert_searched_json == "wrong reference":
                modal1.open()
            elif transfert_searched_json == "wrong pin":
                modal2.open()
            elif transfert_searched_json == "server issue":
                modal3.open()
            else:

                transfert_searched = json.loads(transfert_searched_json)
                agentId = transfert_searched['sentByAgentWithId']
                firstName = transfert_searched['senderFirstName']
                lastName = transfert_searched['senderLastName']
                date = transfert_searched['endedAt'].split("T")[0] + " at " + \
                       transfert_searched['endedAt'].split("T")[1].split(".")[0]
                amount = transfert_searched['transfers'][0]['amount']
                receiverFirstName = transfert_searched['transfers'][0]['receiverFirstName']
                receiverLastName = transfert_searched['transfers'][0]['receiverLastName']

                columns_infos_title[1].header("TRANSFERT INFORMATIONS")

                display_info_transfert()

                space_div()

                columns_button_validate = st.columns((2.2, 1, 2))

                if columns_button_validate[1].button('Validate Payment', type='primary'):
                    modal4.open()
        else:
            modal5.open()


else:
    st.warning("Sorry! This service is not available for now")


if modal1.is_open():
    with modal1.container():
        columns_image = st.columns((2.4, 1, 2))
        img = Image.open("./images/sorry2.png")
        columns_image[1].image(img, width=100)

        html_string = """
        <h1> Not transfert found with this reference </h1>

        <script language="javascript">
          document.querySelector("h1").style.color = "red";
          document.querySelector("h1").style.textAlign = "center";
        </script>
        """
        components.html(html_string)

        columns_button_text = st.columns((2.35, 1, 2))
        columns_button_text[1].write("Please retry :smiley:")
        columns_button_close = st.columns((2.7, 1, 2))
        close_modal1 = columns_button_close[1].button("OK", type='primary')
        if close_modal1:
            modal1.close()

elif modal2.is_open():
    with modal2.container():

        columns_image = st.columns((2.4, 1, 2))
        img = Image.open("./images/sorry2.png")
        columns_image[1].image(img, width=100)

        html_string = '''
        <h1>The code PIN you have entered is incorrect</h1>

        <script language="javascript">
          document.querySelector("h1").style.color = "red";
          document.querySelector("h1").style.textAlign = "center";
        </script>
        '''
        components.html(html_string)

        columns_button_text = st.columns((2.35, 1, 2))
        columns_button_text[1].write("Please retry :smiley:")
        columns_button_close = st.columns((2.7, 1, 2))

        close_modal2 = columns_button_close[1].button("OK", type='primary')
        if close_modal2:
            modal2.close()

elif modal3.is_open():
    with modal3.container():

        columns_image = st.columns((2.4, 1, 2))
        img = Image.open("./images/sorry.png")
        columns_image[1].image(img, width=100)

        html_string = '''
        <h1>Sorry! The service is not available now</h1>

        <script language="javascript">
          document.querySelector("h1").style.color = "red";
          document.querySelector("h1").style.textAlign = "center";
        </script>
        '''
        components.html(html_string)

        columns_button_text = st.columns((2.35, 1, 2))
        columns_button_text[1].write("Please retry :smiley:")
        columns_button_close = st.columns((2.7, 1, 2))

        close_modal3 = columns_button_close[1].button("OK", type='primary')
        if close_modal3:
            modal3.close()

elif modal4.is_open():
    with modal4.container():

        columns_image = st.columns((2.4, 1, 2))
        img = Image.open("./images/money2.png")
        columns_image[1].image(img, width=100)

        html_string = '''
        <h1>Sorry! The service is not available now</h1>

        <script language="javascript">
          document.querySelector("h1").style.color = "red";
          document.querySelector("h1").style.textAlign = "center";
        </script>
        '''
        components.html(html_string)

        columns_button_text = st.columns((2.35, 1, 2))
        columns_button_text[1].write("Please retry :smiley:")
        columns_button_close = st.columns((1, 2, 2))

        close_modal4 = columns_button_close[1].button("Download the Receipt")
        download = columns_button_close[2].button("Finish", type="primary")
        if close_modal4:
            modal4.close()

elif modal5.is_open():
    with modal5.container():

        columns_image = st.columns((2.4, 1, 2))
        img = Image.open("./images/sad-face.png")
        columns_image[1].image(img, width=100)

        html_string = '''
        <h1>you have not filled in all the required fields</h1>

        <script language="javascript">
          document.querySelector("h1").style.color = "red";
          document.querySelector("h1").style.textAlign = "center";
        </script>
        '''
        components.html(html_string)

        columns_button_text = st.columns((2.5, 2, 2))
        columns_button_text[1].write("Please fill in all fields :smiley:")
        columns_button_close = st.columns((2.7, 1, 2))

        close_modal5 = columns_button_close[1].button("OK", type='primary')
        if close_modal5:
            modal5.close()
