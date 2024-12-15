#include <iostream>
using namespace std;

struct Appointment {
    int startHour, startMin, endHour, endMin;
    Appointment* next;
};

Appointment* head = NULL;

void displayFreeSlots() {
    Appointment* temp = head;
    cout << "Free Slots: " << endl;
    while (temp != NULL) {
        cout << "Start Time: " << temp->startHour << ":" << temp->startMin << endl;
        cout << "End Time: " << temp->endHour << ":" << temp->endMin << endl;
        temp = temp->next;
    }
}

void bookAppointment(int startHour, int startMin, int endHour, int endMin) {
    Appointment* newAppointment = new Appointment;
    newAppointment->startHour = startHour;
    newAppointment->startMin = startMin;
    newAppointment->endHour = endHour;
    newAppointment->endMin = endMin;
    newAppointment->next = NULL;

    if (head == NULL) {
        head = newAppointment;
    }
    else {
        Appointment* temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newAppointment;
    }
}

void cancelAppointment(int startHour, int startMin) {
    if (head == NULL) {
        cout << "No appointments booked." << endl;
    }
    else {
        if (head->startHour == startHour && head->startMin == startMin) {
            Appointment* temp = head;
            head = head->next;
            delete temp;
            cout << "Appointment canceled." << endl;
        }
        else {
            Appointment* temp = head;
            Appointment* prev = NULL;
            while (temp != NULL && !(temp->startHour == startHour && temp->startMin == startMin)) {
                prev = temp;
                temp = temp->next;
            }
            if (temp == NULL) {
                cout << "Appointment not found." << endl;
            }
            else {
                prev->next = temp->next;
                delete temp;
                cout << "Appointment canceled." << endl;
            }
        }
    }
}

void sortList() {
    if (head == NULL || head->next == NULL) {
        return;
    }

    Appointment* prev = NULL;
    Appointment* current = head;
    Appointment* temp = NULL;

    bool isSorted = false;
    while (!isSorted) {
        isSorted = true;
        while (current->next != NULL) {
            if (current->startHour > current->next->startHour || (current->startHour == current->next->startHour && current->startMin > current->next->startMin)) {
                if (prev == NULL) {
                    head = current->next;
                    temp = head->next;
                    head->next = current;
                }
                else {
                    prev->next = current->next;
                    temp = current->next->next;
                    current->next->next = current;
                }
                current->next = temp;
                prev = NULL;
                isSorted = false;
            }
            else {
                prev = current;
                current = current->next;
            }
        }
        prev = NULL;
        current = head;
    }
}

int main() {
    bookAppointment(9, 0, 9, 30);
    bookAppointment(10, 0, 10, 30);
    bookAppointment(11, 0, 11, 30);
    bookAppointment(9, 30, 10, 0);

    displayFreeSlots();

    bookAppointment(12, 0, 12, 30);

    displayFreeSlots();

    cancelAppointment(10, 0);

    displayFreeSlots();

    sortList();

    displayFreeSlots();

    return 0;
}

