/*
	Nick Caravaggio

	December 6, 2020

	CS A250 (C++ 2)
	Project 2: With a list of kingdoms, from a text file, organize and append into containers, and sort it in meaningful ways through an easy-to-use CLI-application.
*/

#include "CandidateList.h"

using namespace std;

// Constructor
CandidateList::CandidateList()
{
}

// addCandidate
void CandidateList::addCandidate(const CandidateType& otherCandidate)
{
	candidates.push_back(otherCandidate);
}

// getWinner
int CandidateList::getWinner() const
{
	if (isEmpty())
	{
		cerr << "	List is empty.";
		return 0;
	}
	else
	{
		list<CandidateType>::const_iterator iter = candidates.cbegin();
		list<CandidateType>::const_iterator iterEnd = candidates.cend();
		int idMost = iter->getID();
		int votesMost = iter->getTotalVotes();

		while (iter != iterEnd)
		{
			if (iter->getTotalVotes() > votesMost)
			{
				idMost = iter->getID();
				votesMost = iter->getTotalVotes();
			}
			++iter;
		}
		return idMost;
	}
}

// isEmpty
bool CandidateList::isEmpty() const
{
	return candidates.empty();
}

// searchCandidate
bool CandidateList::searchCandidate(int idNumber) const
{
	list<CandidateType>::const_iterator iter = candidates.cbegin();
	return searchCandidate(idNumber, iter);
}

// Print candidate name
void CandidateList::printCandidateName(int idNumber) const
{
	list<CandidateType>::const_iterator iter;
	if (searchCandidate(idNumber, iter))
	{
		iter->printName();
	}
}

// Printallcandidates
void CandidateList::printAllCandidates() const
{
	if (isEmpty())
	{
		cerr << "	List is empty.";
	}
	else
	{
		list<CandidateType>::const_iterator iter = candidates.cbegin();
		list<CandidateType>::const_iterator iterEnd = candidates.cend();
		while (iter != iterEnd)
		{
			iter->printCandidateInfo();
			cout << endl;
			++iter;
		}
	}
}

// printkingdomvotes
void CandidateList::printKingdomVotes(int idNumber, int index) const
{
	list<CandidateType>::const_iterator iter;
	if (searchCandidate(idNumber, iter))
	{
		cout << "	* " << iter->getVotesByKingdom(index) << "(=>)" << KINGDOMS[index] << endl;
	}
}

// print candidate total votes
void CandidateList::printCandidateTotalVotes(int idNumber) const
{
	list<CandidateType>::const_iterator iter;
	if (searchCandidate(idNumber, iter))
	{
		cout << setw(6) << right << "=>" << " Total Votes: "
			<< iter->getTotalVotes() << endl;
	}
}

// Print final results
void CandidateList::printFinalResults() const
{
	printHeader();
	list<CandidateType>::const_iterator iter = candidates.cbegin();
	list<CandidateType>::const_iterator iterEnd = candidates.cend();
	list<CandidateType>::const_iterator currIter;
	int top = iter->getTotalVotes();
	int currTop = iter->getTotalVotes();

	while (iter != iterEnd)
	{
		if (iter->getTotalVotes() > top)
		{
			currIter = iter;
			top = iter->getTotalVotes();
		}
		++iter;
	}

	printCandidate(currIter, 1);
	iter = candidates.cbegin();
	currIter = candidates.cbegin();
	// static_cast<int>() below?
	int size = static_cast<int>(candidates.size());

	for (int i = 2; i <= size; ++i)
	{
		while (iter != iterEnd)
		{
			if (iter->getTotalVotes() >= currTop && iter->getTotalVotes() < top)
			{
				if (iter->getTotalVotes() == top - 1)
				{
					currTop = iter->getTotalVotes();
					currIter = iter;
					iter = iterEnd;
				}
				else
				{
					currIter = iter;
					currTop = iter->getTotalVotes();
				}
			}
			if (iter != iterEnd)
				++iter;
		}
		top = currTop;
		printCandidate(currIter, i);
		iter = candidates.cbegin();
		currTop = 0;
	}
	cout << "_______________________________________" << endl;
}

// destructor
CandidateList::~CandidateList()
{
}

/*********************************************
* FUNCTION ADDED FOR SELECTION #6
*********************************************/
void CandidateList::printMostVotesPerKingdom() const
{
	list<CandidateType>::const_iterator iter = candidates.cbegin();
	list<CandidateType>::const_iterator iterEnd = candidates.cend();
	list<CandidateType>::const_iterator currentIter = candidates.cbegin();
	int mostVotes = 0;

	// prints header
	cout << "***** TOP VOTES PER KINGDOM *****" << endl;
	cout << "_______________________________________________" << endl;

	for (int i = 0; i < NUM_OF_KINGDOMS; ++i)
	{
		mostVotes = iter->getVotesByKingdom(i);
		while (iter != iterEnd)
		{
			if (iter->getVotesByKingdom(i) > mostVotes)
			{
				currentIter = iter;
				mostVotes = iter->getVotesByKingdom(i);
			}
			++iter;
		}
		iter = candidates.cbegin();
		// assumes first and last name are not longer than 10 characters for the sake of formatting.
		cout << KINGDOMS[i] << endl << setw(5) << right << "-> " << setw(10) << left << currentIter->getLastName() 
			<< setw(10) << left << currentIter->getFirstName() << " | Votes Received: " << currentIter->getVotesByKingdom(i) << " |" 
			<< endl << "_______________________________________________" << endl;
	}
}

// private overloaded searchCandidate
bool CandidateList::searchCandidate(int idNumber, list<CandidateType>::const_iterator& iter) const
{
	iter = find(candidates.begin(), candidates.end(), idNumber);
	if (iter == candidates.end())
	{
		cout << setw(6) << right << "=>" << " ID not in the list." << endl;
		return false;
	}
	return true;
}

// print header function
void CandidateList::printHeader() const
{
	cout << "************ FINAL RESULTS ************" << endl << endl
		<< setw(15) << left << "LAST" << setw(10) << left << "FIRST" << setw(5) << right << "TOTAL" << setw(7) << right << "POS\n"
		<< setw(15) << left << "NAME" << setw(10) << left << "NAME" << setw(5) << right << "VOTES" << setw(7) << right << "#\n"
		<< "_______________________________________" << endl << endl;
}

// print candidate functions
void CandidateList::printCandidate(list<CandidateType>::const_iterator& iter, int pos) const
{
	cout << setw(15) << left << iter->getLastName() << setw(10) << left << iter->getFirstName()
		<< setw(5) << right << iter->getTotalVotes() << setw(7) << right << pos << endl;

	if (pos % 5 == 0)
	{
		cout << "---------------------------------------" << "\n";
	}
}