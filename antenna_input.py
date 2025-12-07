import models.omni_antenna_models as omni
import models.directive_antennas_model as directive


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
            "1": omni.Monopole,
            "2": omni.Dipole,
            "3": omni.FoldedDipole,
            "4": omni.Loop,
            "5": omni.Discone,
            "6": directive.Yagi,
            "7": directive.Helical,
            "8": directive.Parabolic,
            "9": directive.Horn,
            "10": directive.CellSite,
            "11": directive.Microstrip
        }

        #! safe Deafult calue is "Dipole" D=1.64
        antenna_class = antennas.get(choice, omni.Dipole)
        return antenna_class(f, Rr, RL)
