import time
from datetime import datetime as dt
import click
import pandas as pd
import numpy as np

# Removes any warning messages when running code
pd.set_option('mode.chained_assignment', None)

def filter_day(city, day):
    """Filter city data by day of the week.

    INPUT:
    city: pandas.DataFrame. The pandas DataFrame of city data.
    day: str. The day of the week.

    OUTPUT:
    city data filtered by day of the week.
    """
    # create new column for day of the week from Start Time and extract a specific day of the week
    city['day_of_week'] = city['Start Time'].dt.day_name()
    city = city[city['day_of_week'] == day]

    return city

def filter_month(city, month):
    """Filter city data by month of the year.

    INPUT:
    city: pandas.DataFrame. The pandas DataFrame of city data.
    month: str. The month of the year.

    OUTPUT:
    city data filtered by month of the year.
    """
    # create new column for month of the year from Start Time and extract a specific month of the year
    city['month'] = city['Start Time'].dt.month_name()
    city = city[city['month'] == month]

    return city


def filter_both(city, month, day):
    """Filter city data by month of the year and day of the week.

    INPUT:
    city: pandas.DataFrame. The pandas DataFrame of city data.
    month: str. The month of the year.
    day: str. The day of the week.

    OUTPUT:
    city data filtered by month of the year and day of the week.
    """
    # create new columns for month of the year and day of the week from Start Time
    city['month'] = city['Start Time'].dt.month_name()
    city['day_of_week'] = city['Start Time'].dt.day_name()

    #extract a specific day of week for a particular month
    city = city[(city['month'] == month) & (city['day_of_week'] == day)]

    return city


def hours_stats(new_city):
    """Calculate the most popular hour.

    INPUT:
    new_city: pandas.DataFrame. The pandas DataFrame of filtered city data.

    OUTPUT:
    returns the most popular hour and the count of the most popular hour contain in city data filtered.
    """
    # create new column for hour of the day from Start Time
    new_city['hours'] = new_city['Start Time'].dt.hour

    mode_hour = new_city['hours'].mode().iloc[0]

    print('\nCalculating the first statistics...')
    print('Most popular hour:', mode_hour)
    print('Count:', new_city['hours'].value_counts().loc[mode_hour])


def trip_stats(new_city):
    """Calculate the most popular start station, end station and trip.

    INPUT:
    new_city: pandas.DataFrame. The pandas DataFrame of filtered city data.

    OUTPUT:
    returns the most popular start station and the count, the most popular end station and the count and the most popular trip and the count contain in city data filtered.
    """
    mode_start_station = new_city['Start Station'].mode().iloc[0]
    count_mode_start = new_city['Start Station'].value_counts().loc[mode_start_station]

    mode_end_station = new_city['End Station'].mode().iloc[0]
    count_mode_end = new_city['End Station'].value_counts().loc[mode_end_station]

    #  create new column for Trip of from Start Station and End Station
    new_city['Trip'] = new_city['Start Station'] + ' -to- ' + new_city['End Station']

    mode_trip = new_city['Trip'].mode().iloc[0]
    count_mode_trip = new_city['Trip'].value_counts().loc[mode_trip]

    print('\nCalculating the next statistics...')
    print('Most popular start station:', mode_start_station)
    print('Count:', count_mode_start)

    print('\nMost popular end station:', mode_end_station)
    print('Count:', count_mode_end)

    print('\nMost popular trip:', mode_trip)
    print('Count', count_mode_trip)


def trip_time_stats(new_city):
    """Calculate the mean, max and min of Trip Duration.

    INPUT:
    new_city: pandas.DataFrame. The pandas DataFrame of filtered city data.

    OUTPUT:
    returns the mean, max and min of Trip Duration in the filtered city.
    """
    # this converts Trip Duration from seconds to minutes and seconds
    convert_to_minutes = lambda seconds: str(seconds//60) + ' minute(s) ' + str(seconds%60) + ' second(s)'

    mean_trip = new_city['Trip Duration'].mean()
    max_trip = new_city['Trip Duration'].max()
    min_trip = new_city['Trip Duration'].min()

    print('\nCalculating the next statistics...')
    print('Average trip time:', convert_to_minutes(mean_trip))
    print('Maximum trip time:', convert_to_minutes(max_trip))
    print('Least trip time:', convert_to_minutes(min_trip))


def user_type_stats(new_city):
    """Calculate the count of User Type.

    INPUT:
    new_city: pandas.DataFrame. The pandas DataFrame of filtered city data.

    OUTPUT:
    returns the count of Subscriber and Customer in the filtered city data.
    """
    count_subscriber = new_city['User Type'].value_counts().loc['Subscriber']
    count_customer = new_city['User Type'].value_counts().loc['Customer']

    print('\nCalculating the next statistics... User Type')
    print('Numbers of subscribers:', count_subscriber)
    print('Numbers of customers:', count_customer)


def gender_stats(new_city):
    """Calculate the count of Gender.

    INPUT:
    new_city: pandas.DataFrame. The pandas DataFrame of filtered city data.

    OUTPUT:
    returns the count of Male and Female in the filtered city data.
    """
    # gets forward fill of NaN value in Gender column
    new_city['Gender'].fillna(method = 'ffill', inplace = True)

    gender = new_city['Gender'].value_counts()
    print('\nCalculating the next statistics... User Type')
    print("The count of users gender is: \n" + str(gender))


def age_stats(new_city):
    """Calculate the most common, maximum and minimum User Age.

    INPUT:
    new_city: pandas.DataFrame. The pandas DataFrame of filtered city data.

    OUTPUT:
    returns the most common, maximum and minimum User Age in the filtered city data.
    """
    # gets the current year
    current_year = lambda: int(str(dt.today()).split('-')[0])

    # replace NaN value with value in the row before
    new_city['Birth Year'].fillna(new_city['Birth Year'].mean(), inplace = True)

    # create a new column for Age by subtracting current year from Birth Year
    new_city['Age'] = current_year() - new_city['Birth Year']

    mode_age = new_city['Age'].mode()[0]
    max_age = new_city['Age'].max()
    min_age = new_city['Age'].min()

    print('\nCalculating the next statistics... Birth Year')
    print('Most common age:', mode_age)
    print('Maximum age:', max_age)
    print('Minimum age:', min_age)


def user_info(users, new_city):
    """Gets data for specific user(s).

    INPUT:
    users: int. user(s) id seperated by comma.
    new_city: pandas.DataFrame. The pandas DataFrame of city data.

    OUTPUT:
    returns specific user(s) data.
    """
    print(new_city[city['Users ID'].isin(users)])

def main():
    while True:
        try:
            click.clear()
            city_data = str(input('\nHello! Let\'s explore some us bikeshare data! \nWould you like to see data for Chicago, Washington or New york? ')).lower()
            city = pd.read_csv(city_data + '.txt')
            city = city.rename(columns = {'Unnamed: 0' : 'Users ID'})
            city['Start Time'] = pd.to_datetime(city['Start Time'])
            time_filter = input('\nWould you like to filter data by month, day, both or not at all? \nType "None" for no time filter:  ').title()

            if time_filter == 'None':
                start = time.time()
                new_city = city
                hours_stats(new_city)
                trip_stats(new_city)
                trip_time_stats(new_city)
                print('\nFilter:', time_filter)
                print('\nThat took:', time.time() - start, 'second(s)')

                more_info = input('\nWould you like to get users statistics? \n "Yes" or "No": ').title()
                if more_info == 'No':
                    print("")
                elif more_info == 'Yes':
                    user_type_stats(new_city)
                    print('Filter:', time_filter)
                    if city_data != 'washington':
                        gender_stats(new_city)
                        age_stats(new_city)
                        print('\nFilter:', time_filter)


            elif time_filter == 'Day':
                day = input('Which day? \ne.g Monday, Tuesday, ... Sunday : ').title()
                start = time.time()
                new_city = filter_day(city, day)
                hours_stats(new_city)
                trip_stats(new_city)
                trip_time_stats(new_city)
                print('\nFilter:', time_filter)
                print('\nThat took:', time.time() - start, 'second(s)')

                more_info = input('\nWould you like to get users statistics \n "Yes" or "No": ').title()
                if more_info == 'No':
                    print("")
                elif more_info == 'Yes':
                    user_type_stats(new_city)
                    print('Filter:', time_filter)
                    if city_data != 'washington':
                        gender_stats(new_city)
                        age_stats(new_city)
                        print('\nFilter:', time_filter)


            elif time_filter == 'Month':
                month = input('Which month? \ne.g January, February, ... June : ').title()
                start = time.time()
                new_city = filter_month(city, month)
                hours_stats(new_city)
                trip_stats(new_city)
                trip_time_stats(new_city)
                print('\nFilter:', time_filter)
                print('\nThat took:', time.time() - start, 'second(s)')

                more_info = input('\nWould you like to get users statistics \n "Yes" or "No": ').title()
                if more_info == 'No':
                    print("")
                elif more_info == 'Yes':
                    user_type_stats(new_city)
                    print('Filter:', time_filter)
                    if city_data != 'washington':
                        gender_stats(new_city)
                        age_stats(new_city)
                        print('\nFilter:', time_filter)


            elif time_filter == 'Both':
                month = input('Which month? \ne.g January, February, ... June : ').title()
                day = input('Which day? \ne.g Monday, Tuesday, ... Sunday : ').title()
                start = time.time()
                new_city = filter_both(city, month, day)
                hours_stats(new_city)
                trip_stats(new_city)
                trip_time_stats(new_city)
                print('\nFilter:', time_filter)
                print('\nThat took:', time.time() - start, 'second(s)')

                more_info = input('\nWould you like to get users statistics \n "Yes" or "No": ').title()
                if more_info == 'No':
                    print("")
                elif more_info == 'Yes':
                    user_type_stats(new_city)
                    print('Filter:', time_filter)
                    if city_data != 'washington':
                        gender_stats(new_city)
                        age_stats(new_city)
                        print('\nFilter:', time_filter)

        except Exception as e:
            print('\nInvalid input: {}'.format(e))
            print('\nThat took:', time.time() - start, 'second(s)')

        finally:
            try:
                reply = input('\nWould you like to get infomations of specific user(s)  \nType "Yes", "No"  or "Restart": ').lower()
                if reply == "yes":
                    users_list = str(input('Enter user(s) seperated by commas: ')).split(",")
                    users = np.array(users_list, dtype = np.int64)
                    user_info(users, city)
                    next = input('\nWould you like to restart \nType "Yes" or "No" ').lower()
                    if next == "no":
                        break
                elif reply == "no":
                    nex = input('\nWould you like to restart \nType "Yes" or "No" ').lower()
                    if nex == "no":
                        break
                elif reply == "restart":
                    print("\nRestarting")
            except Exception as n:
                print('Invalid input: {}'.format(n))

            print('\nAttempted input')

if __name__ == '__main__':
    main()
