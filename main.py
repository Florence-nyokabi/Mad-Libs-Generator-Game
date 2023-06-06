def beach_story():
    first_input = input("Enter an adjective: ")
    second_input = input("Enter a verb ending in -ing: ")
    third_input = input("Enter an adjective: ")
    forth_input = input("Enter a verb: ")
    fifth_input = input("Enter name of animals in plural: ")
    sixth_input = input("Enter a verb: ")
    seventh_input = input("Enter a verb ending in -ing: ")

    the_beach_story = f"It was a {first_input} day at the beach. The sun was {second_input} and the waves were {third_input}. I decided to {forth_input} in the water, but I didn't realize that there were {fifth_input} swimming around me. I quickly {sixth_input} back to shore and spent the rest of the day {seventh_input} in the sand."
    print(the_beach_story)

def haunted_house():
    haunted_firstinput = input("Enter an adjective: ")
    haunted_secondinput = input("Enter an adjective: ")
    haunted_thirdinput = input("Enter a plural noun: ")
    haunted_forthinput = input("Enter a verb ending in -ing: ")
    haunted_fifthinput = input("Enter an adjective: ")
    haunted_sixthinput = input("Enter an adjective: ")
    haunted_seventhinput = input("Enter a verb ending in -ing: ")
    haunted_eighthinput = input("Enter a verb: ")

    the_haunted_house_story = f"I was walking through the {haunted_firstinput} woods when I stumbled upon a {haunted_secondinput} old house. As I walked inside, I heard {haunted_thirdinput} {haunted_forthinput} and {haunted_fifthinput} whispers. Suddenly, a {haunted_sixthinput} ghost appeared and started {haunted_seventhinput} towards me. I {haunted_eighthinput} out of the house as fast as I could."
    print(the_haunted_house_story)

def superhero():
    superhero_firstinput = input("Enter an adjective: ")
    superhero_secondinput = input("Enter a verb: ")
    superhero_thirdinput = input("Enter a verb: ")
    superhero_forthinput = input("Enter an adjective: ")
    superhero_fifthinput = input("Enter a verb ending in -ing: ")
    superhero_sixthinput = input("Enter a plural noun: ")

    the_superhero_story = f"I woke up one day with {superhero_firstinput} powers. I could {superhero_secondinput} faster than a speeding bullet and {superhero_thirdinput} tall buildings in a single bound. I decided to use my powers for good and became a {superhero_forthinput} superhero. I spent my days {superhero_fifthinput} criminals ans saving the {superhero_sixthinput}."
    print(the_superhero_story)

def road_trip():
    roadtrip_firstinput = input("Enter an adjective: ")
    roadtrip_secondinput = input("Enter a plural noun: ")
    road_trip_thirdinput = input("Enter an adjective: ")
    roadtrip_forthinput = input("Enter a plural noun: ")
    roadtrip_fifthinput = input("Enter an adjective: ")


    the_roadtrip_story = f"My friends and I decided to go on a {roadtrip_firstinput} road trip across the country. We packed our {roadtrip_secondinput} and hit the open road. Along the way, we stopped at {road_trip_thirdinput} landmarks and tried {roadtrip_forthinput}. We even got lost in a {roadtrip_fifthinput} forest, but eventually found our way back to the highway."
    print(the_roadtrip_story)

def fairy_tale():
    fairy_firstinput = input("Enter an adjective: ")
    fairy_secondinput = input("Enter an adjective: ")
    fairy_thirdinput = input("Enter an adjective: ")
    fairy_forthinput = input("Enter verb ending in -ing: ")
    fairy_fifthinput = input("Enter a noun: ")
    fairy_sixthinput = input("Enter an adjective: ")
    fairy_seventhinput = input("Enter a verb ending in -ing: ")

    the_fairy_tale = f"Once upon a time, there was a {fairy_firstinput} princess who lived in a {fairy_secondinput} castle. One day, she met a {fairy_thirdinput} prince who was {fairy_forthinput} in the nearby {fairy_fifthinput}. They fell in love and decided to get married. But first, they had to defeat a {fairy_sixthinput} dragon who was {fairy_seventhinput} the kingdom."
    print(the_fairy_tale)


def main():
    while True:
        print("Welcome to the Mad lib story Generator!")
        print("Please select a story: ")
        print("1. Beach Story")
        print("2. Haunted House Story")
        print("3. Superhero Story" )
        print("4. The Road Trip")
        print("5. The Fairy Tale")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            beach_story()
        elif choice == "2":
            haunted_house()
        elif choice == "3":
            superhero()
        elif choice == "4":
            road_trip()
        elif choice == "5":
            fairy_tale()
        elif choice == "6":
            print("Thank you for using the Mad lib story Generator!")
            break
        else:
            print("Invalid choice. Please try again.")


main()