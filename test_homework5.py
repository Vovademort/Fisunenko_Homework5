#Artur Kazukevich
#13-06-2023
#Grodno-IT-Academy-Python
#Homework-5-Test_Suite

import pytest
import homework5 as hw


class TestGetRanges():
    #testing type of output
    def test_get_ranges_ouput_type(self):
        assert type(hw.get_ranges([1,2])) == type("1-2")
    #testing cases
    def test_get_ranges_case_1(self):
        assert hw.get_ranges([4,7,10]) == "4, 7, 10"
    def test_get_ranges_case_2(self):
        assert hw.get_ranges([9]) == "9"
    def test_get_ranges_case_3(self):
        assert hw.get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) == "0-4, 7-8, 10"
    def test_get_ranges_case_4(self):
        assert hw.get_ranges([2, 3, 8, 9]) == "2-3, 8-9"
    def test_get_range_case_5(self):
        assert hw.get_ranges([6, 7, 8, 9, 10, 11, 56, 57, 58, 59, 60,
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
        76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 632, 633, 634, 635,
        636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647,
        648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659,
        660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671,
        672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683,
        684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695,
        696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707,
        708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719,
        720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731,
        732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743,
        744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755,
        756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767,
        768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779,
        780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791,
        792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803,
        804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815,
        816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827,
        828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839,
        840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851,
        852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863,
        864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875,
        876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887,
        888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899,
        900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911,
        912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923,
        924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935,
        936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947,
        948, 949, 950, 951, 952, 953, 954, 955, 956]) == "6-11, 56-85, 632-956"

class TestPhones():
    #testing types of output
    def test_standardise_phones_case_1(self):
        case = hw.standardise_phones("298884455")
        solution = ["+375298884455"]
        assert type(case) == type(solution)
        assert type(case[0]) == type(solution[0])
        assert case == solution
    def test_standardise_phones_case_2(self):
        case = hw.standardise_phones(*["178884455","80298885555","+375299998877","375299998867"])
        solution = ["+375178884455","+375298885555","+375299998877","+375299998867"]
        assert type(case) == type(solution)
        assert type(case[0]) == type(solution[0])
        assert case == solution
    def test_standardise_phones_case_3(self):
        case = hw.standardise_phones("29888445d","29888445d45","29888445","8884455","884455","84455","845","84","55","5")
        solution = []
        assert type(case) == type(solution)
        assert case == solution
    def test_standardise_phones_case_4(self):
        case = hw.standardise_phones(*[298884455,375297776655,80296665544])
        solution = ["+375298884455","+375297776655","+375296665544"]
        assert type(case) == type(solution)
        assert type(case[0]) == type(solution[0])
        assert type(case) == type(solution)
        assert case == solution

class TestRopeProduct():
    def test_rope_product_case_1(self):
        case = hw.rope_product(1)
        solution = 1
        assert type(case) == type(solution)
        assert case == solution
    def test_rope_product_case_2(self):
        case = hw.rope_product(4)
        solution = 4
        assert type(case) == type(solution)
        assert case == solution
    def test_rope_product_case_3(self):
        case = hw.rope_product(5)
        solution = 6
        assert type(case) == type(solution)
        assert case == solution
    def test_rope_product_case_4(self):
        case = hw.rope_product(11)
        solution = 54
        assert type(case) == type(solution)
        assert case == solution
    def test_rope_product_case_5(self):
        case = hw.rope_product(23)
        solution = 4374
        assert type(case) == type(solution)
        assert case == solution

class TestHandleMultiples():
    def test_handle_multiples_case_1(self):
        case = hw.rope_product(1,2)
        solution = [1, 2]
        assert type(case) == type(solution)
        assert type(case[0]) == type(solution[0])
        assert case == solution

    def test_handle_multiples_case_1(self):
        case = hw.rope_product(*[7,11,23,45,32])
        solution = [12, 54, 4374, 14348907, 118098]
        assert type(case) == type(solution)
        assert type(case[0]) == type(solution[0])
        assert case == solution
