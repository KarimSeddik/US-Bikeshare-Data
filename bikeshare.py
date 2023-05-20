import time
import pandas as pd
pd.set_option('display.max_columns', 100)

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(
            'Which city would you like to explore its data? Chicago or New York City or Washington?\n').lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        else:
            print('You did not enter a valid city name.\n')
            continue

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            '\nWhich month would you like to explore its data? January, February, March, April, May, June or all?\n').title()
        if month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June' or month == 'All':
            break
        else:
            print('You did not enter a valid month name.\n')
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            '\nWhich day would you like to explore its data? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n').title()
        if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday' or day == 'Sunday' or day == 'All':
            break
        else:
            print('You did not enter a valid day name.\n')
            continue

    print('\nYou chose to explore data of:\nCity: {}\nMonth: {}\nDay: {}'.format(
        city.title(), month.title(), day.title()))
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    frequent_month = months_names[df['month'].mode()[0]]
    print('Most Frequent Month:', frequent_month)

    # display the most common day of week
    frequent_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day:', frequent_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    frequent_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', frequent_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    frequent_start = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', frequent_start)

    # display most commonly used end station
    frequent_end = df['End Station'].mode()[0]
    print('Most Frequent End Station:', frequent_end)

    # display most frequent combination of start station and end station trip
    print('Most Frequent Trip: From {} to {}'.format(
        frequent_start, frequent_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = round((df['Trip Duration'].sum())/60/60, 1)
    print('Total Travel Time:', travel_time, 'hours')

    # display mean travel time
    avg_time = round(df['Trip Duration'].mean(), 1)
    print('Average Travel Time:', avg_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    subscribers = df['User Type'].value_counts()['Subscriber']
    customers = df['User Type'].value_counts()['Customer']
    print('Subscribers: {}\nCustomers: {}'.format(subscribers, customers))

    # Display counts of gender
    try:
        males = df['Gender'].value_counts()['Male']
        females = df['Gender'].value_counts()['Female']
        print('\nMales: {}\nFemales: {}'.format(males, females))

    # Display earliest, most recent, and most common year of birth
        print('\nEarliest Year of Birth: {}\nMost Recent Year of Birth: {}\nMost Common Year of Birth: {}'.format(
            int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(df['Birth Year'].mode()[0])))
    except KeyError:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Asks if the user would like to explore raw data."""

    raw_data = input(
        '\nWould you like to explore 5 rows of raw data of your selections? Enter yes or no.\n').lower()
    i = 0
    while True:
        if raw_data == 'no':
            break
        elif raw_data != 'yes' and raw_data != 'no':
            print('\nPlease enter a valid selection.')
            raw_data = input(
                '\nWould you like to explore 5 rows of raw data of your selections? Enter yes or no.\n').lower()
            continue
        elif raw_data == 'yes':
            df2 = df[i:i+5]
            print(df2.head())
        more = input(
            '\nWould you like to explore 5 more rows? Enter yes or no.\n').lower()
        while True:
            if more == 'no':
                break
            elif more != 'yes' and more != 'no':
                print('\nPlease enter a valid selection.')
                more = input(
                    '\nWould you like to explore 5 more rows? Enter yes or no.\n').lower()
                continue
            elif more == 'yes':
                i += 5
                df2 = df[i:i+5]
                print(df2.head())
                more = input(
                    '\nWould you like to explore 5 more rows? Enter yes or no.\n').lower()
                continue
        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input(
            '\nWould you like to restart? Enter yes or no.\n').lower()
        while restart != 'yes' and restart != 'no':
            print('\nPlease enter a valid selection.')
            restart = input(
                '\nWould you like to restart? Enter yes or no.\n').lower()
        if restart == 'yes':
            print('\n')
            continue
        elif restart != 'yes':
            break


if __name__ == "__main__":
    main()
