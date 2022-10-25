import json
import argparse
import difflib

NUM_FACULTY = 59


def parse_args():
    parser = argparse.ArgumentParser(
        description="Check your prelim committee at UMD CS (Last updated: Nov 2022)"
    )
    subparsers = parser.add_subparsers(dest="cmd", required=True)
    ls = subparsers.add_parser("list", description="List field committee members")
    check = subparsers.add_parser(
        "check", description="Validate Chair plus Dept. Rep. combination"
    )

    check.add_argument("-c", "--chair", required=True)
    check.add_argument("-d", "--dept-rep", required=True)

    search = subparsers.add_parser(
        "search", description="Find field committee for given name(s)"
    )
    search.add_argument("-n", "--name", required=True, nargs="*")

    return parser.parse_args()


def main():
    cmsc = CMSC()
    cmsc.test()

    args = parse_args()

    if args.cmd == "list":
        print(
            "{} tenure track faculty in respective field committees:".format(
                cmsc.num_faculty()
            )
        )
        print(cmsc)
    elif args.cmd == "check":
        chair = args.chair
        dr = args.dept_rep
        is_ok, ca, da = cmsc.check_committee(chair=chair, dr=dr)

        status = "OK!" if is_ok else "NOT OK :( "
        msg = (
            f"{status} Your Chair and Dept. Rep. are in different areas.\n"
            f"* Chair:  Prof. {chair}, {ca}\n"
            f"* Dept. Rep: Prof. {dr}, {da}\n"
        )
        print(msg)
    elif args.cmd == "search":
        for n in args.name:
            a = cmsc.get_prof_area(n)
            print(f"Prof. {n}, {a}")


# def num_faculty():


class CMSC:
    DATA_JSON = "data.json"

    def get_prof_area(self, p, do_exit=True):
        a = self.faculty_to_area.get(p)
        if a is None:
            others = difflib.get_close_matches(p, self.faculty_to_area.keys())
            msg = f'ERROR: Faculty with name "{p}" not found, did you mean one of: {others}'
            print(msg)
            return None
        else:
            return a

    def check_committee(self, chair, dr):
        ca = self.get_prof_area(chair)
        da = self.get_prof_area(dr)

        status = (ca is not None) and (da is not None) and (ca != da)
        return (status, ca, da)

    def test(self):
        assert (
            self.num_faculty() == NUM_FACULTY
        ), "Incorrect num faculty, check data.json"
        self.check_all_unique()

    def __init__(self):
        with open(self.DATA_JSON, "r") as f:
            self.data = json.load(f)
        faculty_to_area = {pi: area for area, pis in self.data.items() for pi in pis}
        self.faculty_to_area = faculty_to_area

    def __repr__(self):

        s = json.dumps(self.data, indent=2, sort_keys=True)

        return "CMSC({})\n".format(s)

    def num_faculty(self):
        c = 0
        for k, v in self.data.items():
            c += len(v)
        return c

    def profs(self):
        s = set()
        for k, v in self.data.items():
            for pi in v:
                s.add(pi)
        return s

    def check_all_unique(self):
        fac = self.profs()
        assert len(fac) == self.num_faculty()


if __name__ == "__main__":
    main()
