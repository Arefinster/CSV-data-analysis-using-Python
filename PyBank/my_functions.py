def print_finAnalysis(info, file_path):
    with open(file_path, 'w') as _file:
        _file.write('Financial Analysis\n')
        _file.write('----------------------------\n')
        _file.write(f'Total Months: {info["nMonths"]} \n')        
        _file.write(f'Total: ${info["total_prof_loss"]} \n')        
        _file.write(f'Average Change: ${info["avg_change"]} \n')
        _file.write(f'Greatest Increase in Profits: {info["max_inc"]["date"][0]} (${info["max_inc"]["value"]}) \n')
        _file.write(f'Greatest Decrease in Profits: {info["max_dec"]["date"][0]} (${info["max_dec"]["value"]}) \n')

    print('Financial Analysis\n')
    print('----------------------------\n')
    print(f'Total Months: {info["nMonths"]} \n')        
    print(f'Total: ${info["total_prof_loss"]} \n')        
    print(f'Average Change: ${info["avg_change"]} \n')
    print(f'Greatest Increase in Profits: {info["max_inc"]["date"][0]} (${info["max_inc"]["value"]}) \n')
    print(f'Greatest Decrease in Profits: {info["max_dec"]["date"][0]} (${info["max_dec"]["value"]}) \n')