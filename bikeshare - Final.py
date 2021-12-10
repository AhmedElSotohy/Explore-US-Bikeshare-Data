import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    global month
    global day
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("\nPlease enter city. (chicago, new york city, washington): \n").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        print('\nInvalid city name. Please enter a valid city\n')
        city = input("\nPlease enter city. (chicago, new york city, washington): \n")
        if city in ['chicago', 'new york city', 'washington']:
            break
    # get user input for month (all, january, february, ... , june)
    month = input("Please enter a month. (all, january, february, march, april, may , june): \n").lower()

    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print('\nInvalid entery. Please enter a valid entry\n')
        month = input("Please enter a month. ('january, february, march, april, may , june): \n")
        if month in ['all','january', 'february', 'march', 'april', 'may', 'june']:
            break
        # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please select which day to filter (all, Monday, Tuesday, ... Sunday): \n").lower()

    while day not in ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
        print('Please provide a valid entry\n')
        day = input("Please select which day to filter (all, monday, tuesday, ... sunday): \n")
        if day in ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
            break
    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all' :
        # filter by month to create the new dataframe
        df = df[df.month == month.title()]
    # filter by day of week if applicable
    if day != 'all' :
        # filter by day of week to create the new dataframe
        df = df[df.day_of_week == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # display the most common month
    if month == 'all':
        popular_month = df['Start Time'].dt.month.mode()[0]
        print('\nMost common month is: {}'.format(popular_month))
    # display the most common day of week
    if day == 'all' :
        popular_day = df['day_of_week'].mode()[0]
        print('\nMost common day of week is: {}'.format(popular_day))
    # display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('\nMost popular start hour of the day is: {}'.format(popular_hour))
    # display the most common end hour
    popular_end_hour = df['End Time'].dt.hour.mode()[0]
    print('\nMost common end hour is: {}'.format(popular_end_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nMost common start station is: \n{}'.format(popular_start_station))
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost common end statoin is: \n{}'.format(popular_end_station))
    # display most frequent combination of start station and end station trip
    df['station comb'] = df['Start Station'] + " and " + df['End Station']
    popular_station_comb = df['station comb'].mode()[0]
    print('\nMost common start and end stations are: \n{}'.format(popular_station_comb))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time in seconds
    trip_duration = df['Trip Duration'].sum()

    # display total travel time in minutes
    trip_duration = df['Trip Duration'].sum()
    print('\nTotal trips duration in seconds is: {}'.format(trip_duration))
    print('\nTotal trips duration in minutes is {}'.format(trip_duration/60))
    # display mean travel time
    avg_trip_duration = df['Trip Duration'].mean()
    print('\nAverage trip duration in seconds is: {}'.format(avg_trip_duration))
    print('\nAverage trip duration in minutes is: {}'.format(avg_trip_duration/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts().to_frame()
    print('\nCount of user types is: {}'.format(user_types_count))
    # Display counts of gender
    if 'Gender' in df :
        gender_count = df['Gender'].value_counts().to_frame()
        print('\n Count of genders is: {}'.format(gender_count))
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df :
        earliest_yob = df['Birth Year'].min()
        most_common_yob = df['Birth Year'].mode()[0]
        most_recent_yob = df['Birth Year'].max()

        print('\nEarliest date of birth is: {}'.format(earliest_yob))
        print('\nMost common year of birth is: {}'.format(most_common_yob))
        print('\nMost recent year of birth is: {}'.format(most_recent_yob))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    view_data = input("Woud you like to view 5 rows of individual trip data? Enter yes or no?\n")
    view_data = view_data.lower()
    start_loc1 = 0
    start_loc2 = 5
    while view_data == "yes":
        print(df.iloc[start_loc1:start_loc2])
        start_loc1 += 5
        start_loc2 += 5
        continue_prompt = input("Do you wish to continue?\n").lower()
        while continue_prompt not in ["yes", "no"]:
            print("Invalid input. Please enter Yes or No.\n")
            continue_prompt = input("Do you wish to continue?\n").lower()
            if continue_prompt in ["yes", "no"]:
                break
        if continue_prompt == "yes":
            continue
        elif continue_prompt == "no":
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
