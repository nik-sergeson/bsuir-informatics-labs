package com.lab3.gui;

import com.intellij.uiDesigner.core.GridConstraints;
import com.intellij.uiDesigner.core.GridLayoutManager;
import com.lab3.accessutils.QueueFileHelper;
import com.lab3.accessutils.QueueHelper;
import com.lab3.accessutils.QueueHelperType;
import com.lab3.accessutils.QueueServerHelper;
import com.lab3.server.IServerConnected;
import com.lab3.server.ReserveServer;
import com.lab3.timers.IQueueWaiter;
import com.lab3.timers.ITimerWaiter;
import com.lab3.utils.*;
import com.lab3.timers.TimeCounter;
import com.lab3.timers.Waiter;
import org.apache.log4j.BasicConfigurator;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.event.*;
import java.io.*;



public class Excel implements IQueueWaiter, ITimerWaiter, IShutDown, IServerConnected {
    private JButton openButton;
    private JButton saveButton;
    private JPanel panel1;
    private JButton leaveQueueButton;
    private JLabel infoLabel;
    private JLabel timerLabel;
    private JTable table1;
    private JTextField cellTextField;
    private JButton insertColButton;
    private JButton insertRowButton;
    private JScrollPane tableSrollPane;
    private JTextPane textPane1;
    private JScrollPane textScrollPane;
    private JButton createButton;
    private JButton saveAsButton;
    private JScrollPane unusedPane;
    private JLabel filenamelabel;
    private String path;
    private TimeCounter timer;
    private Waiter waiter;
    private EditorMode editorMode;
    private ExcelTableModel model;
    private String propertyfilepath;
    private String lockfilepath;
    private NotepadModel notepadModel;
    private QueueHelper queueHelper;
    private int timerperiod;
    private QueueHelperType queueHelperType;
    private ReserveServer reserveServer;
    private int remoteUDPport;

    public Excel() {
        BasicConfigurator.configure();
        filenamelabel.setText("");
        SetEditorEnabled(false);
        unusedPane.setEnabled(false);
        SetTableEnabled(false);
        SetButtonsEnabled(true, true, false, false, false);
        infoLabel.setText("");
        timerLabel.setText("");
        final Excel ex = this;
        propertyfilepath = ".\\config.properties";
        PropertiesReader pr = new PropertiesReader(propertyfilepath);
        try {
            timerperiod = pr.GetIntProperty("timer");
            String helper = pr.GetStringProperty("helper");
            if (helper.equals("server"))
                queueHelperType = QueueHelperType.Server;
            else
                queueHelperType = QueueHelperType.File;
            remoteUDPport = pr.GetIntProperty("port");
            if (Boolean.parseBoolean(pr.GetStringProperty("localserver"))) {
                reserveServer = new ReserveServer(this, remoteUDPport);
                new Thread(reserveServer).start();
            }
        } catch (IOException e1) {
            infoLabel.setText("Config file error");
        }
        Runtime.getRuntime().addShutdownHook(new ShutdownHook(this));
        openButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (timer != null) {
                    timer.Pause();
                    TimerResetAction();
                }
                UIManager.put("FileChooser.readOnly", Boolean.TRUE);
                JFileChooser chooser = new JFileChooser();
                FileNameExtensionFilter fileFilter = new FileNameExtensionFilter("txt,xlsx", new String[]{"xlsx", "txt"});
                chooser.setFileFilter(fileFilter);
                chooser.setCurrentDirectory(new File("D:\\Labs\\labs.6term\\SP\\lab3"));
                int result = chooser.showOpenDialog(null);
                File selected = chooser.getSelectedFile();
                if (selected == null || result == JFileChooser.CANCEL_OPTION) {
                    if (timer != null)
                        timer.Reset();
                    return;
                }
                path = selected.getAbsolutePath();
                File selectedf = new File(path);
                if (!selectedf.exists()) {
                    if (timer != null)
                        timer.Reset();
                    return;
                }
                LeaveQueue();
                if (timer != null)
                    timer.Stop();
                filenamelabel.setText(path);
                lockfilepath = path + ".tmp";
                if (queueHelperType == QueueHelperType.File)
                    queueHelper = new QueueFileHelper(lockfilepath, 8);
                else
                    queueHelper = new QueueServerHelper(path, ex);
                if (path.substring(path.length() - 3, path.length()).equals("txt"))
                    editorMode = EditorMode.Text;
                else
                    editorMode = EditorMode.Excel;
                SetButtonsEnabled(true, true, false, true, false);
                AddToQueue();
            }
        });
        saveButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                infoLabel.setText("Access granted");
                if (timer != null)
                    timer.Reset();
                try {
                    if (editorMode == EditorMode.Excel)
                        model.Save();
                    else
                        notepadModel.Save();
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
            }
        });
        leaveQueueButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    queueHelper.DequeFromQueue();
                } catch (IOException e1) {
                    infoLabel.setText("Queue helper error");
                }
                queueHelper = null;
                waiter.disable();
                infoLabel.setText("");
                SetButtonsEnabled(true, true, false, false, false);
                if (editorMode == EditorMode.Excel) {
                    SetTableEnabled(false);
                } else {
                    SetEditorEnabled(false);
                }
            }
        });
        cellTextField.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (timer != null) {
                    timer.Reset();
                }
                if (model != null) {
                    model.setValueAt(cellTextField.getText(), table1.getSelectedRow(), table1.getSelectedColumn());
                    model.fireTableCellUpdated(table1.getSelectedRow(), table1.getSelectedColumn());
                }
            }
        });
        insertRowButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (model != null) {
                    model.setRowCount(model.getRowCount() + 1);
                }
                if (timer != null)
                    timer.Reset();
            }
        });
        insertColButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (model != null) {
                    model.setColumnCount(model.getColumnCount() + 1);
                }
                if (timer != null)
                    timer.Reset();
            }
        });
        createButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (timer != null) {
                    timer.Stop();
                    TimerResetAction();
                }
                infoLabel.setText("");
                filenamelabel.setText("");
                Object[] options1 = {"Excel", "Text"};
                int choice = JOptionPane.showOptionDialog(null, "Excel or Text?", "Choose an option", JOptionPane.YES_NO_OPTION,
                        JOptionPane.INFORMATION_MESSAGE, null, options1, "Excel");
                LeaveQueue();
                if (choice == 0) {
                    SetEditorEnabled(false);
                    SetTableEnabled(true);
                    model = new ExcelTableModel(null, cellTextField);
                    table1.setModel(model);
                    editorMode = EditorMode.Excel;
                    SetButtonsEnabled(true, true, false, true, false);
                } else if (choice == 1) {
                    SetTableEnabled(false);
                    SetEditorEnabled(true);
                    notepadModel = new NotepadModel(textPane1);
                    notepadModel.UpdateView();
                    editorMode = EditorMode.Text;
                    SetButtonsEnabled(true, true, false, true, false);
                }
            }
        });
        saveAsButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (timer != null) {
                    timer.Pause();
                    TimerResetAction();
                }
                JFileChooser chooser = new JFileChooser();
                chooser.setCurrentDirectory(new File("D:\\Labs\\labs.6term\\SP\\lab3"));
                int result = chooser.showSaveDialog(null);
                File selected = chooser.getSelectedFile();
                if (selected == null || result == JFileChooser.CANCEL_OPTION) {
                    if (timer != null)
                        timer.Reset();
                    return;
                }
                String outpath = selected.getAbsolutePath();
                QueueHelper queueoutHelper;
                if (editorMode == EditorMode.Excel) {
                    outpath += ".xlsx";
                    File outfile = new File(outpath);
                    if (queueHelperType == QueueHelperType.File)
                        queueoutHelper = new QueueFileHelper(outpath + ".tmp", 8);
                    else
                        queueoutHelper = new QueueServerHelper(outpath, ex);
                    try {
                        if (outfile.exists() == false || queueoutHelper.AccessGranted()) {
                            if (model != null) {
                                model.setPath(outpath);
                                try {
                                    model.Save();
                                    LeaveQueue();
                                    path = outpath;
                                } catch (IOException e1) {
                                    return;
                                }
                            }
                        } else {
                            if (queueoutHelper.FileIsOpened()) {
                                infoLabel.setText("File is opened in another app");
                                if (timer != null)
                                    timer.Resume();
                                return;
                            } else {
                                if (model != null) {
                                    model.setPath(outpath);
                                    try {
                                        model.Save();
                                        LeaveQueue();
                                        path = outpath;
                                    } catch (IOException e1) {
                                        return;
                                    }
                                }
                            }
                        }
                    } catch (IOException e1) {
                        e1.printStackTrace();
                    }
                    filenamelabel.setText(path);
                } else {
                    outpath += ".txt";
                    File outfile = new File(outpath);
                    if (queueHelperType == QueueHelperType.File)
                        queueoutHelper = new QueueFileHelper(outpath + ".tmp", 8);
                    else
                        queueoutHelper = new QueueServerHelper(outpath, ex);
                    try {
                        if (outfile.exists() == false || queueoutHelper.AccessGranted()) {
                            if (notepadModel != null) {
                                notepadModel.setPath(path);
                                try {
                                    notepadModel.Save();
                                    LeaveQueue();
                                    path = outpath;
                                } catch (IOException e1) {
                                    return;
                                }
                            }
                        } else {
                            if (queueoutHelper.FileIsOpened()) {
                                infoLabel.setText("File is opened in another app");
                                if (timer != null)
                                    timer.Resume();
                                return;
                            } else {
                                if (model != null) {
                                    model.setPath(outpath);
                                    try {
                                        model.Save();
                                        LeaveQueue();
                                        path = outpath;
                                    } catch (IOException e1) {
                                        return;
                                    }
                                }
                            }
                        }
                    } catch (IOException e1) {
                        e1.printStackTrace();
                    }
                    filenamelabel.setText(path);
                }
                lockfilepath = path + ".tmp";
                if (queueHelperType == QueueHelperType.File)
                    queueHelper = queueoutHelper;
                else
                    queueHelper = queueoutHelper;
                try {
                    queueHelper.AppendToQueue();
                } catch (Exception e1) {
                    infoLabel.setText("Queue helper error");
                }
                SetButtonsEnabled(true, true, true, true, false);
                if (timer == null) {
                    timer = new TimeCounter(timerperiod, timerperiod / 2, ex);
                    new Thread(timer).start();
                } else
                    timer.Resume();
            }
        });
        table1.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                if (timer != null)
                    timer.Reset();
                JTable target = (JTable) e.getSource();
                int row = target.getSelectedRow();
                int column = target.getSelectedColumn();
                model.DisplayCellValue(row, column);
            }
        });
        textPane1.addKeyListener(new KeyAdapter() {
            public void keyPressed(KeyEvent e) {
                if (timer != null)
                    timer.Reset();
                super.keyPressed(e);
                if (notepadModel != null)
                    notepadModel.UpdateModel();
            }
        });
        tableSrollPane.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                if (timer != null)
                    timer.Reset();
                super.mouseClicked(e);
            }
        });
        textScrollPane.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                if (timer != null)
                    timer.Reset();
                super.mouseClicked(e);
            }
        });
        textPane1.addFocusListener(new FocusAdapter() {
            @Override
            public void focusGained(FocusEvent e) {
                if (timer != null)
                    timer.Reset();
                super.focusGained(e);
            }
        });
    }

    public void ShutDownAction() {
        if (queueHelper != null)
            try {
                queueHelper.DequeFromQueue();
            } catch (IOException e) {
                infoLabel.setText("Queue helper error");
            }
        else
            System.out.print("null");
        if (lockfilepath != null) {
            File f = new File(lockfilepath);
            if (f.exists() && f.length() == 0)
                f.delete();
        }
        if (reserveServer != null)
            try {
                reserveServer.Stop();
            } catch (InterruptedException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
    }

    public void Disconect() {
        try {
            if (queueHelper != null)
                queueHelper.DequeFromQueue();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public ServerAddress GetServerAddress() {
        return reserveServer.GetRemoteServerAddress();
    }

    public ServerAddress GetLocalAddress() {
        return reserveServer.GetLocalServerAddress();
    }

    private void SetButtonsEnabled(boolean openbutton, boolean createbutton, boolean savebutton, boolean saveasbutton, boolean leavebutton) {
        openButton.setEnabled(openbutton);
        createButton.setEnabled(createbutton);
        saveButton.setEnabled(savebutton);
        saveAsButton.setEnabled(saveasbutton);
        leaveQueueButton.setEnabled(leavebutton);
    }

    public void Switch(ReserveServer reserveServer) {
        this.reserveServer = reserveServer;
    }

    public void SetEditorEnabled(boolean mode) {
        textPane1.setEnabled(mode);
        textPane1.setVisible(mode);
        textScrollPane.setEnabled(mode);
        textScrollPane.setVisible(mode);
        unusedPane.setVisible(!mode);
    }

    public void SetTableEnabled(boolean mode) {
        table1.setEnabled(mode);
        table1.setVisible(mode);
        tableSrollPane.setEnabled(mode);
        tableSrollPane.setVisible(mode);
        insertColButton.setEnabled(mode);
        insertColButton.setVisible(mode);
        insertRowButton.setEnabled(mode);
        insertRowButton.setVisible(mode);
        cellTextField.setEnabled(mode);
        cellTextField.setVisible(mode);
        unusedPane.setVisible(!mode);
    }

    public void GetAccessAction() {
        infoLabel.setText("Access granted");
        if (editorMode == EditorMode.Excel)
            try {
                model.Refresh();
            } catch (IOException e) {
                e.printStackTrace();
            }
        else
            try {
                notepadModel.Refresh();
            } catch (IOException e) {
                e.printStackTrace();
            }
        SetButtonsEnabled(true, true, true, true, false);
        timer = new TimeCounter(timerperiod, timerperiod / 2, this);
        if (editorMode == EditorMode.Excel)
            model.setTimerCounter(timer);
        new Thread(timer).start();
        if (editorMode == EditorMode.Excel)
            model.setReadonlymode(false);
        else
            notepadModel.setReadonlymode(false);
    }

    public void TimerNotifyAction(long sec) {
        timerLabel.setText("Time left: " + Long.toString(sec / 60) + " mins and " + Long.toString(sec % 60) + " s");
    }

    public void TimerResetAction() {
        timerLabel.setText("");
    }

    public void TimerInteraptionAction() {
        timerLabel.setText("");
    }

    public void TimerStopAction() {
        LeaveQueue();
        timerLabel.setText("");
        SetButtonsEnabled(true, true, false, false, false);
        if (editorMode == EditorMode.Excel) {
            SetTableEnabled(false);
        } else {
            SetEditorEnabled(false);
        }
        infoLabel.setText("Thank for editing file");
    }

    private void LeaveQueue() {
        if (waiter != null)
            waiter.disable();
        if (queueHelper != null) {
            try {
                queueHelper.DequeFromQueue();
            } catch (IOException e) {
                infoLabel.setText("Queue helper error");
            }
            queueHelper = null;
            File f = new File(lockfilepath);
            if (f.length() == 0) {
                f.delete();
            }
        }
    }

    public boolean AccessGranted() {
        if (queueHelper == null)
            return false;
        try {
            return queueHelper.AccessGranted();
        } catch (IOException e) {
            infoLabel.setText("Queue helper error");
        }
        return false;
    }

    public void AddToQueue() {
        try {
            queueHelper.AppendToQueue();
        } catch (Exception e) {
            infoLabel.setText("Queue helper error");
            return;
        }
        try {
            if (editorMode == EditorMode.Excel) {
                SetEditorEnabled(false);
                SetTableEnabled(true);
                model = new ExcelTableModel(path, null, cellTextField);
                table1.setModel(model);
            } else {
                SetTableEnabled(false);
                SetEditorEnabled(true);
                notepadModel = new NotepadModel(path, textPane1);
                notepadModel.UpdateView();
            }
        } catch (IOException e) {
            SetButtonsEnabled(true, true, false, false, false);
            infoLabel.setText("File doesnt exist");
            try {
                queueHelper.DequeFromQueue();
            } catch (IOException e1) {
                infoLabel.setText("Queue helper error");
            }
        }
        if (!AccessGranted()) {
            infoLabel.setText("You've been placed in queue");
            waiter = new Waiter(path, this);
            new Thread(waiter).start();
            if (editorMode == EditorMode.Excel)
                model.setReadonlymode(true);
            else
                notepadModel.setReadonlymode(true);
            SetButtonsEnabled(true, true, false, false, true);
        } else {
            infoLabel.setText("Access granted");
            SetButtonsEnabled(true, true, true, true, false);
            GetAccessAction();
        }
    }

    public static void main(String[] args) {
        final JFrame frame = new JFrame("Excel");
        frame.setPreferredSize(new Dimension(800, 500));
        final Excel ex = new Excel();
        frame.setContentPane(ex.panel1);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent winEvt) {
                ex.ShutDownAction();
                System.exit(0);
            }
        });

        frame.setVisible(true);
    }

    {
// GUI initializer generated by IntelliJ IDEA GUI Designer
// >>> IMPORTANT!! <<<
// DO NOT EDIT OR ADD ANY CODE HERE!
        $$$setupUI$$$();
    }

    /**
     * Method generated by IntelliJ IDEA GUI Designer
     * >>> IMPORTANT!! <<<
     * DO NOT edit this method OR call it in your code!
     *
     * @noinspection ALL
     */
    private void $$$setupUI$$$() {
        panel1 = new JPanel();
        panel1.setLayout(new GridLayoutManager(8, 5, new Insets(0, 0, 0, 0), -1, -1));
        tableSrollPane = new JScrollPane();
        panel1.add(tableSrollPane, new GridConstraints(2, 0, 1, 5, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_BOTH, GridConstraints.SIZEPOLICY_CAN_SHRINK | GridConstraints.SIZEPOLICY_CAN_GROW, GridConstraints.SIZEPOLICY_CAN_SHRINK | GridConstraints.SIZEPOLICY_WANT_GROW, null, new Dimension(384, 419), null, 0, false));
        table1 = new JTable();
        table1.setAutoCreateRowSorter(false);
        table1.setAutoResizeMode(0);
        tableSrollPane.setViewportView(table1);
        textScrollPane = new JScrollPane();
        panel1.add(textScrollPane, new GridConstraints(3, 0, 1, 5, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_BOTH, GridConstraints.SIZEPOLICY_CAN_SHRINK | GridConstraints.SIZEPOLICY_WANT_GROW, GridConstraints.SIZEPOLICY_CAN_SHRINK | GridConstraints.SIZEPOLICY_WANT_GROW, null, new Dimension(384, 23), null, 0, false));
        textPane1 = new JTextPane();
        textScrollPane.setViewportView(textPane1);
        infoLabel = new JLabel();
        infoLabel.setText("Label");
        panel1.add(infoLabel, new GridConstraints(5, 0, 1, 5, GridConstraints.ANCHOR_SOUTHWEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(119, 16), null, 0, false));
        timerLabel = new JLabel();
        timerLabel.setText("Label");
        panel1.add(timerLabel, new GridConstraints(6, 0, 1, 5, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        openButton = new JButton();
        openButton.setText("   Open   ");
        panel1.add(openButton, new GridConstraints(0, 0, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        createButton = new JButton();
        createButton.setText("  Create  ");
        panel1.add(createButton, new GridConstraints(0, 1, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        saveButton = new JButton();
        saveButton.setText("   Save   ");
        panel1.add(saveButton, new GridConstraints(0, 2, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        saveAsButton = new JButton();
        saveAsButton.setText("Save as");
        panel1.add(saveAsButton, new GridConstraints(0, 3, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        leaveQueueButton = new JButton();
        leaveQueueButton.setText("Leave Queue");
        panel1.add(leaveQueueButton, new GridConstraints(0, 4, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        insertColButton = new JButton();
        insertColButton.setText("+col");
        panel1.add(insertColButton, new GridConstraints(1, 4, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        insertRowButton = new JButton();
        insertRowButton.setText("+row");
        panel1.add(insertRowButton, new GridConstraints(1, 3, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        cellTextField = new JTextField();
        panel1.add(cellTextField, new GridConstraints(1, 0, 1, 3, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_WANT_GROW, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(150, -1), null, 0, false));
        unusedPane = new JScrollPane();
        panel1.add(unusedPane, new GridConstraints(4, 0, 1, 5, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_BOTH, GridConstraints.SIZEPOLICY_CAN_SHRINK | GridConstraints.SIZEPOLICY_WANT_GROW, GridConstraints.SIZEPOLICY_CAN_SHRINK | GridConstraints.SIZEPOLICY_WANT_GROW, null, null, null, 0, false));
        filenamelabel = new JLabel();
        filenamelabel.setText("Label");
        panel1.add(filenamelabel, new GridConstraints(7, 0, 1, 5, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
    }

    /**
     * @noinspection ALL
     */
    public JComponent $$$getRootComponent$$$() {
        return panel1;
    }
}
