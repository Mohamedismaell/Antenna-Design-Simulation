import antenna_models


class AntennaInput:

    def get_antenna(self):

        f = float(input("Enter frequency (Hz): "))
        Rr = float(input("Enter radiation resistance Rr: "))
        RL = float(input("Enter loss resistance RL: "))

        print("\n--- Select Antenna Type ---")
        print("OMNI / WIRE")
        print("1 - Monopole (Whip)")
        print("2 - Dipole")
        print("3 - Folded Dipole")
        print("4 - Loop")
        print("5 - Discone")

        print("\nDirective")
        print("6 - Yagi Array")
        print("7 - Helical")
        print("8 - Parabolic Reflector")
        print("9 - Horn")
        print("10 - Cell Site")
        print("11 - Microstrip Patch")

        choice = input("\nEnter number: ")

        antennas = {
            "1": antenna_models.Monopole,
            "2": antenna_models.Dipole,
            "3": antenna_models.FoldedDipole,
            "4": antenna_models.Loop,
            "5": antenna_models.Discone,
            "6": antenna_models.Yagi,
            "7": antenna_models.Helical,
            "8": antenna_models.Parabolic,
            "9": antenna_models.Horn,
            "10": antenna_models.CellSite,
            "11": antenna_models.Microstrip
        }

        #! safe Deafult calue is "Dipole" D=1.64
        antenna_class = antennas.get(choice, antenna_models.Dipole)
        return antenna_class(f, Rr, RL)
