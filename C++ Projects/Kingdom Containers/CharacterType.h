/*
	Nick Caravaggio

	December 6, 2020

	CS A250 (C++ 2)
	Project 2: With a list of kingdoms, from a text file, organize and append into containers, and sort it in meaningful ways through an easy-to-use CLI-application.
*/

#ifndef CHARACTERTYPE_H
#define CHARACTERTYPE_H

#include <iostream>
#include <string>

class CharacterType
{
public:
	// Default constructor
	CharacterType() : id(0) {}
	// Overloaded constructor
	CharacterType(const std::string& fName, const std::string& lName, int idx);

	// setCharacterInfo
	void setCharacterInfo(const std::string& fName, const std::string& lName, int idx);

	// getFirstName
	std::string getFirstName() const;
	// getLastName
	std::string getLastName() const;
	// getID
	int getID() const;

	// printName
	void printName() const;
	// printCharacterInfo
	void printCharacterInfo() const;
	// printID
	void printID() const;

	// Destructor
	~CharacterType();

private:
	std::string firstName;
	std::string lastName;
	int id;
};

#endif 