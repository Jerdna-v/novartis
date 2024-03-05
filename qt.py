

#ifndef DESIGNMVTQPC_H
#define DESIGNMVTQPC_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QTableWidget *edutabel;
    QLabel *edulabel;
    QLabel *edulabel_2;
    QTableWidget *edutabel_2;
    QFrame *skilllframe;
    QLabel *shift;
    QLabel *motivated;
    QLabel *self;
    QLabel *learn;
    QLabel *other;
    QLabel *shift2;
    QLabel *motivated2;
    QLabel *self2;
    QLabel *learn2;
    QLabel *other2;
    QFrame *skilllframe_2;
    QLabel *english;
    QLabel *slovene;
    QLabel *other_2;
    QLabel *english2;
    QLabel *slovene2;
    QLabel *other2_2;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1171, 795);
        MainWindow->setAnimated(true);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        edutabel = new QTableWidget(centralwidget);
        edutabel->setObjectName(QStringLiteral("edutabel"));
        edutabel->setGeometry(QRect(70, 120, 251, 221));
        edutabel->setRowCount(0);
        edulabel = new QLabel(centralwidget);
        edulabel->setObjectName(QStringLiteral("edulabel"));
        edulabel->setGeometry(QRect(150, 70, 108, 28));
        QFont font;
        font.setPointSize(14);
        edulabel->setFont(font);
        edulabel->setLayoutDirection(Qt::LeftToRight);
        edulabel->setAlignment(Qt::AlignCenter);
        edulabel_2 = new QLabel(centralwidget);
        edulabel_2->setObjectName(QStringLiteral("edulabel_2"));
        edulabel_2->setGeometry(QRect(130, 390, 121, 28));
        edulabel_2->setFont(font);
        edulabel_2->setLayoutDirection(Qt::LeftToRight);
        edulabel_2->setAlignment(Qt::AlignCenter);
        edutabel_2 = new QTableWidget(centralwidget);
        edutabel_2->setObjectName(QStringLiteral("edutabel_2"));
        edutabel_2->setGeometry(QRect(70, 440, 251, 221));
        edutabel_2->setRowCount(0);
        skilllframe = new QFrame(centralwidget);
        skilllframe->setObjectName(QStringLiteral("skilllframe"));
        skilllframe->setGeometry(QRect(440, 90, 561, 281));
        skilllframe->setAutoFillBackground(false);
        skilllframe->setFrameShape(QFrame::StyledPanel);
        skilllframe->setFrameShadow(QFrame::Raised);
        skilllframe->setLineWidth(5);
        skilllframe->setMidLineWidth(0);
        shift = new QLabel(skilllframe);
        shift->setObjectName(QStringLiteral("shift"));
        shift->setGeometry(QRect(40, 20, 171, 41));
        shift->setFont(font);
        motivated = new QLabel(skilllframe);
        motivated->setObjectName(QStringLiteral("motivated"));
        motivated->setGeometry(QRect(30, 70, 181, 41));
        motivated->setFont(font);
        self = new QLabel(skilllframe);
        self->setObjectName(QStringLiteral("self"));
        self->setGeometry(QRect(40, 120, 141, 41));
        self->setFont(font);
        learn = new QLabel(skilllframe);
        learn->setObjectName(QStringLiteral("learn"));
        learn->setGeometry(QRect(40, 170, 151, 41));
        learn->setFont(font);
        other = new QLabel(skilllframe);
        other->setObjectName(QStringLiteral("other"));
        other->setGeometry(QRect(70, 220, 61, 41));
        other->setFont(font);
        shift2 = new QLabel(skilllframe);
        shift2->setObjectName(QStringLiteral("shift2"));
        shift2->setGeometry(QRect(350, 20, 101, 41));
        shift2->setFont(font);
        motivated2 = new QLabel(skilllframe);
        motivated2->setObjectName(QStringLiteral("motivated2"));
        motivated2->setGeometry(QRect(350, 70, 101, 41));
        motivated2->setFont(font);
        self2 = new QLabel(skilllframe);
        self2->setObjectName(QStringLiteral("self2"));
        self2->setGeometry(QRect(350, 120, 101, 41));
        self2->setFont(font);
        learn2 = new QLabel(skilllframe);
        learn2->setObjectName(QStringLiteral("learn2"));
        learn2->setGeometry(QRect(350, 170, 101, 41));
        learn2->setFont(font);
        other2 = new QLabel(skilllframe);
        other2->setObjectName(QStringLiteral("other2"));
        other2->setGeometry(QRect(350, 220, 101, 41));
        other2->setFont(font);
        skilllframe_2 = new QFrame(centralwidget);
        skilllframe_2->setObjectName(QStringLiteral("skilllframe_2"));
        skilllframe_2->setGeometry(QRect(440, 390, 561, 281));
        skilllframe_2->setAutoFillBackground(false);
        skilllframe_2->setFrameShape(QFrame::StyledPanel);
        skilllframe_2->setFrameShadow(QFrame::Raised);
        skilllframe_2->setLineWidth(5);
        skilllframe_2->setMidLineWidth(0);
        english = new QLabel(skilllframe_2);
        english->setObjectName(QStringLiteral("english"));
        english->setGeometry(QRect(90, 30, 171, 41));
        english->setFont(font);
        slovene = new QLabel(skilllframe_2);
        slovene->setObjectName(QStringLiteral("slovene"));
        slovene->setGeometry(QRect(90, 110, 181, 41));
        slovene->setFont(font);
        other_2 = new QLabel(skilllframe_2);
        other_2->setObjectName(QStringLiteral("other_2"));
        other_2->setGeometry(QRect(100, 210, 61, 41));
        other_2->setFont(font);
        english2 = new QLabel(skilllframe_2);
        english2->setObjectName(QStringLiteral("english2"));
        english2->setGeometry(QRect(350, 30, 101, 41));
        english2->setFont(font);
        slovene2 = new QLabel(skilllframe_2);
        slovene2->setObjectName(QStringLiteral("slovene2"));
        slovene2->setGeometry(QRect(350, 110, 101, 41));
        slovene2->setFont(font);
        other2_2 = new QLabel(skilllframe_2);
        other2_2->setObjectName(QStringLiteral("other2_2"));
        other2_2->setGeometry(QRect(350, 220, 101, 41));
        other2_2->setFont(font);
        MainWindow->setCentralWidget(centralwidget);
        skilllframe->raise();
        edutabel->raise();
        edulabel->raise();
        edulabel_2->raise();
        edutabel_2->raise();
        skilllframe_2->raise();

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        edulabel->setText(QApplication::translate("MainWindow", "Education:", nullptr));
        edulabel_2->setText(QApplication::translate("MainWindow", "Experience:", nullptr));
        shift->setText(QApplication::translate("MainWindow", "Shift experience", nullptr));
        motivated->setText(QApplication::translate("MainWindow", "Motivated/flexible", nullptr));
        self->setText(QApplication::translate("MainWindow", "Self-initiative", nullptr));
        learn->setText(QApplication::translate("MainWindow", "Eager to learn", nullptr));
        other->setText(QApplication::translate("MainWindow", "Other", nullptr));
        shift2->setText(QApplication::translate("MainWindow", "true", nullptr));
        motivated2->setText(QApplication::translate("MainWindow", "false", nullptr));
        self2->setText(QApplication::translate("MainWindow", "true", nullptr));
        learn2->setText(QApplication::translate("MainWindow", "true", nullptr));
        other2->setText(QApplication::translate("MainWindow", "none", nullptr));
        english->setText(QApplication::translate("MainWindow", "English", nullptr));
        slovene->setText(QApplication::translate("MainWindow", "Slovene", nullptr));
        other_2->setText(QApplication::translate("MainWindow", "Other", nullptr));
        english2->setText(QApplication::translate("MainWindow", "true", nullptr));
        slovene2->setText(QApplication::translate("MainWindow", "true", nullptr));
        other2_2->setText(QApplication::translate("MainWindow", "none", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // DESIGNMVTQPC_H
