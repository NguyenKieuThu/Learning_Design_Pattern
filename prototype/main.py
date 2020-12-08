"""
clone one instance of one class (the result is the same with deepcopy function of copy module)
ref: https://refactoring.guru/design-patterns/prototype
"""

import shape

if __name__=='__main__':
    rec_origin = shape.Rectangle(10, 5, 'red', 20, 10)
    print("==Rectangle==")
    rec_origin.show_object()
    print("Clone other rectangle is copy-rectangle")
    rec_copy = rec_origin.clone()
    rec_copy.show_object()
    print("Change central of origin rectangle")
    rec_origin.change_central(6, 6)
    rec_origin.show_object()
    print("Re-show information of copy-rectangle")
    rec_copy.show_object()
