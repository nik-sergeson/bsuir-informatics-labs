using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel;

public class Ticket:BuisnessEntity,INotifyPropertyChanged
{
    private int _aeroplaneid;
    private int _ownerid;
    private int _flightid;
    private int _cost;
    private int _id;
    private int _seat;

    public int AeroplaneID
    {
        get { return _aeroplaneid; }
        set { SetProperty(ref _aeroplaneid, value, "AeroplaneID"); }
    }

    public int OwnerID
    {
        get { return _ownerid; }
        set
        {
            SetProperty(ref _ownerid, value, "OwnerID");
        }
    }

    public int FlightID
    {
        get { return _flightid; }
        set { SetProperty(ref _flightid, value, "FlightID"); }
    }

    public int Cost
    {
        get { return _cost; }
        set { SetProperty(ref _cost, value, "Cost"); }
    }

    public override int ID
    {
        get { return _id; }
        set { SetProperty(ref _id, value, "ID"); }
    }
    public int Seat
    {
        get { return _seat; }
        set { SetProperty(ref _seat, value, "Seat"); }
    }

    public Ticket()
    {
        _aeroplaneid = -1;
        _ownerid = -1;
        _flightid = -1;
        _cost = 0;
        _id = -1;
        _seat = -1;
    }

    public Ticket(int aeroplaneid, int ownerid, int flightid, int cost, int id, int seat)
    {
        _aeroplaneid = aeroplaneid;
        _ownerid = ownerid;
        _flightid = flightid;
        _cost = cost;
        _id = id;
        _seat = seat;
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
