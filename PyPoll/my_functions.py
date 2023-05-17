def vote_counter(data):
    """
    The parameter 'data' is in matrix format or list of lists.
    column 0 = voter id
    column 1 = state
    column 2 = candidate's name
    Access the information in 'data' as data[rows_index][cols_index]
    """
    candidate_list = []
    voter_count_list = []
    v = 0
    while v < len(data):
    #for v in range(len(data)):
        curr_candidate = data[v][2]
        if curr_candidate in candidate_list:
            c_idx = candidate_list.index(curr_candidate)
            r = v # start a new iterator from here
            vote_count = 0 # initialize a vote count from here
            while r < len(data) and data[r][2] == curr_candidate:
                r += 1
                vote_count += 1
            voter_count_list[c_idx] += vote_count
        else:
            candidate_list.append(curr_candidate)
            r = v # start a new iterator from here
            vote_count = 0 # initialize a vote count from here
            while data[r][2] == curr_candidate:
                r += 1
                vote_count += 1
            voter_count_list.append(vote_count)
        v = r # update the outer loop index
    vote_percentage = [round((vc/len(data))*100,3) for vc in voter_count_list]    
    election_results = zip(candidate_list, vote_percentage, voter_count_list)    
    return list(election_results) 
                

def print_ElectionResults(info, file_path):
    with open(file_path, 'w') as _file:
        _file.write('Election Results\n')
        print('Election Results\n')
        _file.write('----------------------------\n')
        print('----------------------------\n')
        _file.write(f'Total Votes: {info["nVotes"]} \n')        
        print(f'Total Votes: {info["nVotes"]} \n')
        for row in info["results"]:
            _file.write(f'{row[0]}: {row[1]}% ({row[2]})\n')
            print(f'{row[0]}: {row[1]}% ({row[2]})')
        _file.write('----------------------------\n')
        print('----------------------------\n')
        _file.write(f'Winner: {info["winner_name"]}\n')
        print(f'Winner: {info["winner_name"]}')
        _file.write('----------------------------\n')
        print('----------------------------\n')