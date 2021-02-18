using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel;

public class Station:BuisnessEntity, INotifyPropertyChanged
{
    private DateTime _departingtime;
    private DateTime _arrivaltime;
    private string _name;
    private string _country;
    private int _id;

    public DateTime DepartingTime
    {
        get { return _departingtime; }
        set { SetProperty(ref _departingtime, value, "DepartingTime"); }
    }

    public DateTime ArrivalTime
    {
        get { return _arrivaltime; }
        set { SetProperty(ref _arrivaltime, value, "ArrivalTime"); }
    }

    public string Name
    {
        get { return _name; }
        set { SetProperty(ref _name, value, "Name"); }
    }

    public string Country
    {
        get { return _country; }
        set { SetProperty(ref _country, value, "Country"); }
    }

    public override int ID
    {
        get { return _id; }
        set { SetProperty(ref _id, value, "ID"); }
    }

    public Station()
    {
        _departingtime = DateTime.MinValue;
        _arrivaltime = DateTime.MinValue;
        _name = "Noname";
        _country = "Noname";
        _id = -1;
    }

    public Station(DateTime departingtime, DateTime arrivaltime, string name, string country, int id)
    {
        _departingtime = departingtime;
        _arrivaltime = arrivaltime;
        _name = name;
        _country = country;
        _id = id;
    }

    public event PropertyChangedEventHandler PropertyChanged;
    private void SetProperty<T>(ref T field, T value, string name)
    {
        if (!EqualityComparer<T>.Default.Equals(field, value))
        {
            field = value;
            var handler = PropertyChanged;
            if (handler != null)
            {
                handler(this, new PropertyChangedEventArgs(name));
            }
        }
    }
}