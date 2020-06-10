  ## room_book
  * book_room{"facility_type": "rooms"}
    - room_booking_form
    - form{"name": "room_booking_form"}
    - form{"name": "null"}
  * confirm
    - utter_room_confirm


  ## room_clean_time
  * request_room_cleaning{"service": "clean"}
    - room_clean_form
    - form{"name": "room_clean_form"}
    - form{"name": "null"}

  ## just book room, continue
  * book_room{"facility_type": "rooms"}
    - room_booking_form
    - form{"name": "room_booking_form"}
  * faq
    - respond_faq
    - room_booking_form
    - form{"name": null}
  * confirm
    - utter_room_confirm

  ## just clean room, continue
  * book_room{"facility_type": "rooms"}
    - room_clean_form
    - form{"name": "room_clean_form"}
  * faq
    - respond_faq
    - room_clean_form
    - form{"name": null}

  ## Questions from faq
  * faq
    - respond_faq

  ## bot_challenge
  * bot_challenge
    - utter_iamabot

  ## out of scope
  * out_of_scope
    - utter_out_of_scope
