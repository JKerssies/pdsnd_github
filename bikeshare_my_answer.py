import time as t
import numpy as np
import pandas as pd
 
CITY_DATA = { 'chicago': 'chicago.csv',
              'nyc': 'new_york_city.csv',
              'washington': 'washington.csv' }
 
def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.
 
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print ('Hello! Let\'s explore major US bikeshare data!')
    print ('')
    #Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    t.sleep(1)
    while True:
        print ("Which city do you want to explore bikeshare data from? (Please choose: chicago, nyc, or washington)\n")
        city = input("Chicago, NYC or Washington?\n").lower()
        if city not in ("chicago", "nyc", "washington"):
            print("\nOops, seems like data for that city is not available. Please choose 1 of these: chicago, nyc, or washington\n") 
            continue
        else:
            break
        
    print("\nGreat! How do you want to filter your data? Please choose: Month, day, both, or none\n")
    
    #Get user input for month (all, january, february, ... , june)
    data_filter = input("Month, day, or both?\n").lower()
    
    while True:
        if data_filter not in ("month", "day", "both", "none"):
            print("\nOops, seems like your request can't be fulfilled. Please choose: Month, day, both, or none\n")
            data_filter = input("Month, day, both, or none?\n")
        elif data_filter == "month":
            print("Which month do you want to explore?\n")
            month = input("January, february, march, april, may, june or all?\n").lower()
            day = 'all'
            while True:
                if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                    print("\nOops, seems like your request can't be fulfilled. Please choose: january, february, march, april, may, june or all\n")
                    month = input("January, february, march, april, may, june or all?\n").lower()
                else:
                    break
            break
        elif data_filter == "day":
            print("Which day do you want to explore?\n")
            day = input("Monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n").lower()
            month = 'all'
            while True:
                if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
                    print("\nOops, seems like your request can't be fulfilled. Please choose: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all\n")
                    day = input("Monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n").lower()
                else:
                    break
            break
        elif data_filter == "both":
            print("Which month do you want to explore?\n")
            month = input("January, february, march, april, may, june or all?\n").lower()
            while True:
                if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                    print("\nOops, seems like your request can't be fulfilled. Please choose: january, february, march, april, may, june or all\n")
                    month = input("January, february, march, april, may, june or all?\n").lower()
                else:
                    break
                    
            print("Now which day do you want to explore?\n")
            day = input("Monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n").lower()
            while True:
                if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
                    print("\nOops, seems like your request can't be fulfilled. Please choose: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all\n")
                    day = input("Monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n").lower()
                else:
                    break 
            break    
 
    print("--->  ", city)
    print("--->  ", month)
    print("--->  ", day)
    return city, month, day
 
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
 
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
 
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
 
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
 
    # filter by day of week if applicable
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df
 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    start_time = t.time()
  
    print('\nCalculating The Most Frequent Times of Travel...\n')
    print('')
 
    #display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
 
    print('The Most Common Month for travel is:', common_month)
    print('')
    
    #display the most common day of week
    df['week'] = df['Start Time'].dt.week
    common_week = df['week'].mode()[0]
 
    print('The Most Common day of week for travel is:', common_week)
    print('')
    
    #display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
 
    print('Tne Most Common Start Hour for travel is:', common_hour)
    print('')
 
    print("\nThis took %s seconds." % (t.time() - start_time))
    print('-'*40)
    
          
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    print('')
    start_time = t.time()
 
    #display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
 
    print('The Most Common Start Station for travel is:', common_start_station)
    print('')
 
    #display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
 
    print('The Most Common End Station for travel is:', common_end_station)
    print('')
 
    #display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] + ' to ' + df['End Station'] 
    common_station_combo = df['combo'].mode()[0]
 
    print('The Most common Combination of start station and end station for travel is:', common_station_combo)
    print('')
 
    print("\nThis took %s seconds." % (t.time() - start_time))
    print('-'*40)
 
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
 
    print('\nCalculating Trip Duration...\n')
    start_time = t.time()
 
    #display total travel time
    total_travel_time = df['Trip Duration'].sum()
 
    print('The Total Travel Time in your filtered data is:', total_travel_time)
    print('')
 
    #display mean travel time
    average = df['Trip Duration'].mean()
 
    print('The mean Travel Time in your filtered data is:', average)
    print('')
 
    print("\nThis took %s seconds." % (t.time() - start_time))
    print('-'*40)
 
def user_stats(df):
    """Displays statistics on bikeshare users."""
 
    print('\nCalculating User Stats...\n')
    start_time = t.time()
 
    #Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The count of user types is:', user_types)
    print('')
    
    #Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('The count of gender for users is:', gender)
        print('')
    else:
        print("Gender information is not available for this city!")
 
    #Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest_birth_year = df['Birth_Year'].min()
        print('The Earliest Birth Year in your filtered data is:', earliest_birth_year)
        print('')
        recent_birth_year = df['Birth Year'].max()
 
        print('The most recent Birth Year in your filtered data is:', recent_birth_year)
        print('')
 
        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common Birth Year in your filtered data is:', common_birth_year)
        print('')
    else:
        print("Birth year information is not available for this city!")
 
    print("\nThis took %s seconds." % (t.time() - start_time))
    print('-'*40)
    
def data(df): 
    """ Displays 10 rows of raw data at a time """ 
    line_number = 0 
    print("\nDo you want to see some data example of your dataset?\n")
    answer = input("Yes or no?\n").lower()
    if answer not in ['yes', 'no']: 
        print("\nOops, seems like your answer is not valid. Please choose yes or no\n")
        answer = input("Yes or no?\n").lower()
    elif answer == 'yes': 
        while True: 
            line_number += 10
            print(df.iloc[line_number : line_number + 10]) 
            print("\nDo you want to see more raw data?\n")
            continues = input("Yes or no?\n").strip().lower() 
            if continues == 'no':    
                break
    elif answer == 'no':
        return    
    
def main():
    city = ""
    month = 0
    day = 0
    
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)
 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)
 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    
if __name__ == "__main__":
    main()