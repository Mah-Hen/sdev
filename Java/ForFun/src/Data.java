public class Data {
        private Deck cardDeck;
    public Data(){
        cardDeck = new Deck();
        Card C1 = new Card("Griffin", 4, 5, "None");
        cardDeck.addCard(C1);
        Card C2 = new Card("Kappa", 2, 3, "Darkness");
        cardDeck.addCard(C2);
        Card C3 = new Card("Ghoul", 6, 4,"None");
        cardDeck.addCard(C3);
        Card C4 = new Card("Moth Man", 6, 3,"None");
        cardDeck.addCard(C4);
        Card C5 = new Card("Chubracabra", 6, 7, "None");
        cardDeck.addCard(C5);
        Card C6 = new Card("Red Cap", 5, 3, "None");
        cardDeck.addCard(C6);
        Card C7 = new Card("Minotaur", 7, 4, "None");
        cardDeck.addCard(C7);
        Card C8 = new Card("Adlet", 4, 4, "None");
        cardDeck.addCard(C8);
        Card C9 = new Card("Basilisk", 5, 4, "Venom");
        cardDeck.addCard(C9);
        Card C10 = new Card("Sphinx", 2, 7, "Magic");
        cardDeck.addCard(C10);
        Card C11 = new Card("Cacu", 3, 7, "Burn");
        cardDeck.addCard(C11);
        Card C12 = new Card("Scorpion Man", 5, 5, "Venom");
        cardDeck.addCard(C12);
        //Card C13 = new Card("Harpy", "Trap");
        //cardDeck.addCard(C13);
        //Card C14 = new Card("Pandora's Box", "Trap");
        //cardDeck.addCard(C14);
        Card C15 = new Card("Elf", 3, 4, "Magic");
        cardDeck.addCard(C15);
        Card C16 = new Card("Antero Vipunen", 5, 5, "Magic");
        cardDeck.addCard(C16);
        Card C17 = new Card("Sirin", 6, 5, "None");
        cardDeck.addCard(C17);
        Card C18 = new Card("Capacun", 6, 4, "Darkness");
        cardDeck.addCard(C18);
        Card C19 = new Card("Scylla", 5, 3, "");
        cardDeck.addCard(C19);
        Card C20 = new Card("Ammit", 7, 4 ,"None");
        cardDeck.addCard(C20);
        /* 
        Card C14 = new Card("Namazu");
        cardDeck.addCard(C14);
        */
    }

    public Deck getData(){
        return cardDeck;
    }

}
