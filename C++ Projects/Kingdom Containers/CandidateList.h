/*
	Nick Caravaggio

	December 6, 2020

	CS A250 (C++ 2)
	Project 2: With a list of kingdoms, from a text file, organize and append into containers, and sort it in meaningful ways through an easy-to-use CLI-application.
*/

#ifndef CANDIDATELIST_H
#define CANDIDATELIST_H

#include "CandidateType.h"
#include <iostream>
#include <string>
#include <iomanip>
#include <list>

class CandidateList: public CandidateType
{
public:
	// Default constructor
	CandidateList();

	// addCandidate
	void addCandidate(const CandidateType& otherCandidate);

	// getWinner
	int getWinner() const;

	// isEmpty
	bool isEmpty() const;
	// searchCandidate with id only
	bool searchCandidate(int idNumber) const;

	// prints candidate name from idNumber
	void printCandidateName(int idNumber) const;
	// printAllCandidates
	void printAllCandidates() const;
	// prints kingdom votes from idNumber
	void printKingdomVotes(int idNumber, int index) const;
	// prints candidate total votes from id number parameter
	void printCandidateTotalVotes(int idNumber) const;

	// prints final results function
	void printFinalResults() const;
	// Destructor
	~CandidateList();

	/*********************************************
	* FUNCTION ADDED FOR SELECTION #6
	*********************************************/
	void printMostVotesPerKingdom() const;

private:
	// searchcandidate with id and iterator
	bool searchCandidate(int idNumber, std::list<CandidateType>::const_iterator& iter) const;

	// prints the output header.
	void printHeader() const;
	//printCandidate with iterator and position in parameters
	void printCandidate(std::list<CandidateType>::const_iterator& iter, int position) const;

	std::list<CandidateType> candidates;
};

#endif
