/*
	Nick Caravaggio

	December 6, 2020

	CS A250 (C++ 2)
	Project 2: With a list of kingdoms, from a text file, organize and append into containers, and sort it in meaningful ways through an easy-to-use CLI-application.
*/

#include "CandidateList.h"

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

void createCandidateList(std::ifstream& infile, 
	CandidateList& candidateList)
{
	int id = 0;
	int allVotes[NUM_OF_KINGDOMS];
	std::string  fName, lName;

	infile >> id;

	while (id != -999)
	{
		CandidateType newCandidate;

		infile >> fName;
		infile >> lName;
		newCandidate.setCharacterInfo(fName, lName, id);

		for (int i = 0; i < NUM_OF_KINGDOMS; ++i)
		{
			infile >> allVotes[i];
			newCandidate.updateVotesByKingdom(i, allVotes[i]);
		}

		candidateList.addCandidate(newCandidate);

		infile >> id;
	}
}

void readCandidateData(CandidateList& candidateList)
{
	std::ifstream infile;

	infile.open("candidates_data.txt");

	if (!infile)
	{
		std::cerr << "Input file does not exist.\n";
		exit(1);
	}

	createCandidateList(infile, candidateList);

	infile.close();
}
