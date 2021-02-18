using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel;

public class Flight:BuisnessEntity, INotifyPropertyChanged
{
    private int _id;
    private int _cost;
    private int _departingpoint;
    private int _arrivalpoint;

    public override int ID
    {
        get { return _id; }
        set { SetProperty(ref _id, value, "ID"); }
    }

    public int Cost
    {
        get { return _cost; }
        set { SetProperty(ref _cost, value, "Cost"); }
    }

    public int DepartingPoint
    {
        get { return _departingpoint; }
        set { SetProperty(ref _departingpoint, value, "DepartingPoint"); }
    }

    public int ArrivalPoint
    {
        get { return _arrivalpoint; }
        set { SetProperty(ref _arrivalpoint, value, "ArrivalPoint"); }
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

    public Flight(int id,int cost,int departingpoint,int arrivalpoint)
    {
        _id = id;
        _cost = cost;
        _departingpoint = departingpoint;
        _arrivalpoint = arrivalpoint;
    }

    public Flight()
    {
        _id = -1;
        _cost = 0;
        _departingpoint = -1;
        _arrivalpoint = -1;
    }
}
