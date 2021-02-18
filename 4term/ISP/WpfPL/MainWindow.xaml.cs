using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using IDAL;
using BLL;
using System.Collections.Specialized;
using System.ComponentModel;

namespace WpfPL
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        BindingList<BuisnessEntity> sourcelist;

        public MainWindow()
        {
            InitializeComponent();
            dataGrid1.AutoGenerateColumns = false;
            dataGrid1.CanUserAddRows = false;
            dataGrid1.BorderThickness = new Thickness(2);
            dataGrid1.RowHeaderWidth = 0;
            dataGrid1.ItemsSource = sourcelist;
            comboBox1.SelectedIndex = 0;
        }

        private void CopyToSourceList<T>(List<T> lst) where T:BuisnessEntity
        {
            sourcelist=new BindingList<BuisnessEntity>();
            foreach (var x in lst)
                sourcelist.Add(x);
            dataGrid1.ItemsSource = sourcelist;
        }

        private int FindIndex(int id)
        {
            int i;
            for (i = 0; i < sourcelist.Count; i++)
                if (sourcelist[i].ID == id)
                    return i;
            return -1;
        }
        private void ComboBox_SelectionChanged_1(object sender, SelectionChangedEventArgs e)
        {
            if (comboBox1.SelectedIndex != -1)
            {
                DeleteBox.Visibility = Visibility.Visible;
                DeleteButton.Visibility = Visibility.Visible;
                FindButton.Visibility = Visibility.Visible;
                FindBox.Visibility = Visibility.Visible;
                dataGrid1.Columns.Clear();
                StackPanel2.Children.Clear();
                StackPanel1.Children.Clear();
            }
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    FindBox.Text = "Enter Flight ID";
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "ID",
                        Binding = new Binding("ID") { Mode = BindingMode.TwoWay },
                        IsReadOnly = true
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "FlightID",
                        Binding = new Binding("FlightID") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Capacity",
                        Binding = new Binding("Capacity") { Mode = BindingMode.TwoWay }
                    });
                    CopyToSourceList<Aeroplane>(AeroplaneLogic.ReadAll());
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "FlightID",
                        FontSize = 14
                    });
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Capacity",
                        FontSize = 14
                    });
                    StackPanel2.Children.Add(new TextBox());
                    StackPanel2.Children.Add(new Label());
                    StackPanel2.Children.Add(new TextBox());
                    break;
                case 1:
                    FindBox.Text = "Enter client ID";
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "ID",
                        Binding = new Binding("ID") { Mode = BindingMode.TwoWay },
                        IsReadOnly = true
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Name",
                        Binding = new Binding("Name") { Mode = BindingMode.TwoWay }
                    });
                    CopyToSourceList<Client>(ClientLogic.ReadAll());
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Name",
                        FontSize = 14
                    });
                    StackPanel2.Children.Add(new TextBox());
                    StackPanel2.Children.Add(new Label());
                    break;
                case 2:
                    FindBox.Text = "Enter arrival point";
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "FlightID",
                        Binding = new Binding("ID") { Mode = BindingMode.TwoWay },
                        IsReadOnly = true
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Cost",
                        Binding = new Binding("Cost") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "DepartingPoint",
                        Binding = new Binding("DepartingPoint") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "ArrivalPoint",
                        Binding = new Binding("ArrivalPoint") { Mode = BindingMode.TwoWay }
                    });
                    CopyToSourceList<Flight>(FlightLogic.ReadAll());
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Cost",
                        FontSize = 14
                    });
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Departing Point",
                        FontSize = 14
                    });
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Arrival Point",
                        FontSize = 14
                    });
                    StackPanel2.Children.Add(new TextBox());
                    StackPanel2.Children.Add(new Label());
                    StackPanel2.Children.Add(new TextBox());
                    StackPanel2.Children.Add(new Label());
                    StackPanel2.Children.Add(new TextBox());
                    break;
                case 3:
                    FindBox.Text = "Enter name";
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "ID",
                        Binding = new Binding("ID") { Mode = BindingMode.TwoWay },
                        IsReadOnly = true
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Departing Time",
                        Binding = new Binding("DepartingTime") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Arrival Time",
                        Binding = new Binding("ArrivalTime") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Name",
                        Binding = new Binding("Name") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Country",
                        Binding = new Binding("Country") { Mode = BindingMode.TwoWay }
                    });
                    CopyToSourceList<Station>(StationLogic.ReadAll());
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Departing Time",
                        FontSize = 14
                    });
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Arrival Time",
                        FontSize = 14
                    });
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Name",
                        FontSize = 14
                    });
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Country",
                        FontSize = 14
                    });
                    StackPanel2.Children.Add(new TextBox());
                    StackPanel2.Children.Add(new Label());
                    StackPanel2.Children.Add(new TextBox());
                    StackPanel2.Children.Add(new Label());
                    StackPanel2.Children.Add(new TextBox());
                    StackPanel2.Children.Add(new Label());
                    StackPanel2.Children.Add(new TextBox());
                    break;
                case 4:
                    FindBox.Text = "Enter Ticket ID";
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "ID",
                        Binding = new Binding("ID") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "AeroplaneID",
                        Binding = new Binding("AeroplaneID") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "OwnerID",
                        Binding = new Binding("OwnerID") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "FlightID",
                        Binding = new Binding("FlightID") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Cost",
                        Binding = new Binding("Cost") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Seat",
                        Binding = new Binding("Seat") { Mode = BindingMode.TwoWay }
                    });
                    CopyToSourceList<Ticket>(TicketLogic.ReadAll());
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Aeroplane ID",
                        FontSize = 14
                    });
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Owner ID",
                        FontSize = 14
                    });
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Flight ID",
                        FontSize = 14
                    });
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Cost",
                        FontSize = 14
                    });
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "ID",
                        FontSize = 14
                    });
                    StackPanel1.Children.Add(new Label()
                    {
                        Content = "Seat",
                        FontSize = 14
                    });
                    StackPanel2.Children.Add(new TextBox());
                    StackPanel2.Children.Add(new Label());
                    StackPanel2.Children.Add(new TextBox());
                    StackPanel2.Children.Add(new Label());
                    StackPanel2.Children.Add(new TextBox());
                    StackPanel2.Children.Add(new Label());
                    StackPanel2.Children.Add(new TextBox());
                    StackPanel2.Children.Add(new Label());
                    StackPanel2.Children.Add(new TextBox());
                    StackPanel2.Children.Add(new Label());
                    StackPanel2.Children.Add(new TextBox());
                    break;
            }
        }

        private void FindButton_Click(object sender, RoutedEventArgs e)
        {
            int ID;
            StackPanel1.Children.Clear();
            StackPanel2.Children.Clear();
            dataGrid1.Columns.Clear();
            AddButton.Visibility = Visibility.Hidden;
            DeleteBox.Visibility = Visibility.Hidden;
            DeleteButton.Visibility = Visibility.Hidden;
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    if (!Int32.TryParse(FindBox.Text, out ID))
                    {
                        MessageBox.Show("Incorrect ID");
                    }
                    else
                    {
                        dataGrid1.Columns.Add(new DataGridTextColumn()
                        {
                            Header = "ID",
                            Binding = new Binding("ID") { Mode = BindingMode.TwoWay },
                            IsReadOnly = true
                        });
                        dataGrid1.Columns.Add(new DataGridTextColumn()
                        {
                            Header = "FlightID",
                            Binding = new Binding("FlightID") { Mode = BindingMode.TwoWay }
                        });
                        dataGrid1.Columns.Add(new DataGridTextColumn()
                        {
                            Header = "Capacity",
                            Binding = new Binding("Capacity") { Mode = BindingMode.TwoWay }
                        });
                        CopyToSourceList<Aeroplane>(AeroplaneLogic.FindByFlight(ID));
                    }
                    break;
                case 1:
                    if (!Int32.TryParse(FindBox.Text, out ID))
                    {
                        MessageBox.Show("Incorrect ID");
                    }
                    else
                    {
                        dataGrid1.Columns.Add(new DataGridTextColumn()
                        {
                            Header = "ID",
                            Binding = new Binding("ID") { Mode = BindingMode.TwoWay },
                            IsReadOnly = true
                        });
                        dataGrid1.Columns.Add(new DataGridTextColumn()
                        {
                            Header = "Name",
                            Binding = new Binding("Name") { Mode = BindingMode.TwoWay }
                        });
                        List<Client> clients = new List<Client>();
                        clients.Add(ClientLogic.Read(ID));
                        CopyToSourceList<Client>(clients);
                    }
                    break;
                case 2:
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "FlightID",
                        Binding = new Binding("FlightID") { Mode = BindingMode.TwoWay },
                        IsReadOnly = true
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Cost",
                        Binding = new Binding("Cost") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "DepartingPoint",
                        Binding = new Binding("DepartingPoint") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "ArrivalPoint",
                        Binding = new Binding("ArrivalPoint") { Mode = BindingMode.TwoWay }
                    });
                    CopyToSourceList<Flight>(FlightLogic.FindByArrivalPoint(FindBox.Text));
                    break;
                case 3:
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "ID",
                        Binding = new Binding("ID") { Mode = BindingMode.TwoWay },
                        IsReadOnly = true
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Departing Time",
                        Binding = new Binding("DepartingTime") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Arrival Time",
                        Binding = new Binding("Arrival Time") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Name",
                        Binding = new Binding("Name") { Mode = BindingMode.TwoWay }
                    });
                    dataGrid1.Columns.Add(new DataGridTextColumn()
                    {
                        Header = "Country",
                        Binding = new Binding("Country") { Mode = BindingMode.TwoWay }
                    });
                    CopyToSourceList<Station>(StationLogic.FindByName(FindBox.Text));                    
                    break;
                case 4:
                    if (!Int32.TryParse(FindBox.Text, out ID))
                    {
                        MessageBox.Show("Incorrect ID");
                    }
                    else
                    {
                        dataGrid1.Columns.Add(new DataGridTextColumn()
                        {
                            Header = "ID",
                            Binding = new Binding("ID") { Mode = BindingMode.TwoWay }
                        });
                        dataGrid1.Columns.Add(new DataGridTextColumn()
                        {
                            Header = "AeroplaneID",
                            Binding = new Binding("AeroplaneID") { Mode = BindingMode.TwoWay }
                        });
                        dataGrid1.Columns.Add(new DataGridTextColumn()
                        {
                            Header = "OwnerID",
                            Binding = new Binding("OwnerID") { Mode = BindingMode.TwoWay }
                        });
                        dataGrid1.Columns.Add(new DataGridTextColumn()
                        {
                            Header = "FlightID",
                            Binding = new Binding("FlightID") { Mode = BindingMode.TwoWay }
                        });
                        dataGrid1.Columns.Add(new DataGridTextColumn()
                        {
                            Header = "Cost",
                            Binding = new Binding("Cost") { Mode = BindingMode.TwoWay }
                        });
                        dataGrid1.Columns.Add(new DataGridTextColumn()
                        {
                            Header = "Seat",
                            Binding = new Binding("Seat") { Mode = BindingMode.TwoWay }
                        });
                        CopyToSourceList<Ticket>(TicketLogic.GetAvailableTickets(ID));
                    }
                    break;
            }
        }

        private void AddButton_Click(object sender, RoutedEventArgs e)
        {
            TextBox z1, z2, z3, z4, z5;
            DateTime date;
            int temp;
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    z1 = (TextBox)StackPanel2.Children[0];
                    z2 = (TextBox)StackPanel2.Children[2];
                    if (int.TryParse(z1.Text, out temp) && int.TryParse(z2.Text, out temp))
                    {
                        Aeroplane plane = new Aeroplane(((sourcelist.Count > 0) ? (sourcelist[sourcelist.Count - 1].ID + 1) : 1), int.Parse(z1.Text), int.Parse(z2.Text));
                        AeroplaneLogic.AddPlane(plane);
                        sourcelist.Add(plane);
                    }
                    else
                        MessageBox.Show("Incorrect data");
                    break;
                case 1:
                    z1 = (TextBox)StackPanel2.Children[0];
                    Client client = new Client(z1.Text, ((sourcelist.Count > 0) ? (sourcelist[sourcelist.Count - 1].ID + 1) : 1));
                    ClientLogic.AddClient(client);
                    sourcelist.Add(client);
                    break;
                case 2:
                    z1 = (TextBox)StackPanel2.Children[0];
                    z2 = (TextBox)StackPanel2.Children[2];
                    z3 = (TextBox)StackPanel2.Children[4];
                    if (Int32.TryParse(z1.Text, out temp) && Int32.TryParse(z2.Text, out temp) && Int32.TryParse(z3.Text, out temp))
                    {
                        Flight flight = new Flight(((sourcelist.Count > 0) ? (sourcelist[sourcelist.Count - 1].ID + 1) : 1), int.Parse(z1.Text), int.Parse(z2.Text), int.Parse(z3.Text));
                        FlightLogic.AddFlight(flight);
                        sourcelist.Add(flight);
                    }
                    else
                        MessageBox.Show("Incorrect data");
                    break;
                case 3:
                    z1 = (TextBox)StackPanel2.Children[0];
                    z2 = (TextBox)StackPanel2.Children[2];
                    z3 = (TextBox)StackPanel2.Children[4];
                    z4 = (TextBox)StackPanel2.Children[6];
                    if (DateTime.TryParse(z1.Text, out date) && DateTime.TryParse(z2.Text, out date))
                    {
                        Station station = new Station(DateTime.Parse(z1.Text), DateTime.Parse(z2.Text), z3.Text, z4.Text, ((sourcelist.Count > 0) ? (sourcelist[sourcelist.Count - 1].ID + 1) : 1));
                        StationLogic.AddStation(station);
                        sourcelist.Add(station);
                    }
                    else
                        MessageBox.Show("Incorrect data");
                    break;
                case 4:
                    z1 = (TextBox)StackPanel2.Children[0];
                    z2 = (TextBox)StackPanel2.Children[2];
                    z3 = (TextBox)StackPanel2.Children[4];
                    z4 = (TextBox)StackPanel2.Children[6];
                    z5 = (TextBox)StackPanel2.Children[8];
                    if (Int32.TryParse(z1.Text, out temp) && Int32.TryParse(z2.Text, out temp) && Int32.TryParse(z3.Text, out temp) && Int32.TryParse(z4.Text, out temp) && Int32.TryParse(z5.Text, out temp))
                    {
                        Ticket ticket = new Ticket(int.Parse(z1.Text), int.Parse(z2.Text), int.Parse(z3.Text), int.Parse(z4.Text), ((sourcelist.Count > 0) ? (sourcelist[sourcelist.Count - 1].ID + 1) : 1), int.Parse(z5.Text));
                        TicketLogic.AddTicket(ticket);
                        sourcelist.Add(ticket);
                    }
                    else
                        MessageBox.Show("Incorrect data");
                    break;
            }
        }

        private void DeleteButton_Click(object sender, RoutedEventArgs e)
        {
            int ID;
            if (Int32.TryParse(DeleteBox.Text, out ID))
            {
                sourcelist.RemoveAt(FindIndex(ID));
                switch (comboBox1.SelectedIndex)
                {
                    case 0:
                        AeroplaneLogic.DeletePlane(ID);
                        break;
                    case 1:
                        ClientLogic.DeleteClient(ID);
                        break;
                    case 2:
                        FlightLogic.DeleteFlight(ID);
                        break;
                    case 3:
                        StationLogic.DeleteStation(ID);
                        break;
                    case 4:
                        TicketLogic.DeleteTicket(ID);
                        break;
                }
            }
            else
                MessageBox.Show("Недопустимый ID");
        }

        private bool isManualEditCommit;

        private void dataGrid1_RowEditEnding(object sender, DataGridRowEditEndingEventArgs e)
        {

            if (!isManualEditCommit)
            {
                isManualEditCommit = true;
                DataGrid grid = (DataGrid)sender;
                grid.CommitEdit(DataGridEditingUnit.Row, true);
                isManualEditCommit = false;
            }
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    AeroplaneLogic.Update((Aeroplane)sourcelist[e.Row.GetIndex()]);
                    break;
                case 1:
                    ClientLogic.UpdateClient((Client)sourcelist[e.Row.GetIndex()]);
                    break;
                case 2:
                    FlightLogic.UpdateFlight((Flight)sourcelist[e.Row.GetIndex()]);
                    break;
                case 3:
                    StationLogic.UpdateStation((Station)sourcelist[e.Row.GetIndex()]);
                    break;
                case 4:
                    TicketLogic.Update((Ticket)sourcelist[e.Row.GetIndex()]);
                    break;
            }

        }

        private void dataGrid1_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {

        }
    }
}
