int main(int argc, char* argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int solution_no = 1;
    int part_no = 1;
    if (argc >= 2) {
        part_no = stoi(argv[1]);
    } else if (argc >= 3) {
        solution_no = stoi(argv[2]);
    }
    unique_ptr<Solution> sol;
    switch (solution_no) {
        case 1:
            sol = make_unique<Solution_01>();
            break;
        default:
            cout << "Solution " << solution_no << " does not exist\n";
            exit(1);
    }
    sol->run(part_no);
    return 0;
}
