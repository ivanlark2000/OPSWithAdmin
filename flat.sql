
CREATE TABLE public.flats (
    flat_id numeric NOT NULL,
    address text NOT NULL,
    price integer NOT NULL,
    district character varying(50) NOT NULL,
    number_of_rooms smallint NOT NULL,
    time_of_add date DEFAULT now(),
    square_of_kitchen numeric(4,1),
    living_space numeric(4,1),
    floor smallint NOT NULL,
    furniture text,
    technics text,
    balcony_or_loggia character varying(50),
    room_type character varying(50),
    ceiling_height numeric(3,1),
    bathroom character varying(50),
    widow character varying(50),
    repair character varying(50),
    seilling_method character varying(50),
    transaction_type character varying(50),
    decorating character varying(50),
    total_space numeric(4,1) NOT NULL,
    status character varying(15) DEFAULT 'active'::character varying
);


